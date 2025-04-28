from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import requests
from user_funcs import create_user, verify_user, get_user, update_user, delete_user
from ai_funcs import analyze_interaction, get_medication_info

app = Flask(__name__)
CORS(app)  # This allows your React frontend to make requests to this backend


def normalize_name(name):
    return name.strip().lower()

def check_name(medication):
    """
    Check if a medication exists in the FDA database and return information.
    """
    medication = medication.strip().lower()
    print(f"Checking medication: {medication}")
    
    # Search for both generic and brand names
    url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{medication}+OR+openfda.brand_name:{medication}&limit=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "results" not in data or len(data["results"]) == 0:
            print(f"Medication not found: {medication}")
            return medication.capitalize() + " not found."
        
        result = data["results"][0]
        openfda = result.get("openfda", {})
        
        # Get medication names
        generic_names = openfda.get("generic_name", [])
        brand_names = openfda.get("brand_name", [])
        
        generic_name = generic_names[0] if generic_names else medication
        brand_name = brand_names[0] if brand_names else ""
        
        # Build response message
        info = f"{generic_name.capitalize()} found."
        if brand_name and brand_name.lower() != generic_name.lower():
            info += f" Brand name: {brand_name}."
            
        print(f"Medication found: {info}")
        return info
            
    except Exception as e:
        print(f"Error checking FDA database: {str(e)}")
        return medication.capitalize() + " not found (Error)."

def check_if_medication_exists(medication):
    """Simple helper function to check if a medication exists in the FDA database"""
    medication = medication.strip().lower()
    url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{medication}+OR+openfda.brand_name:{medication}&limit=1"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"FDA API error: {response.status_code}")
            return False
            
        data = response.json()
        if "results" not in data:
            print("No results field in FDA API response")
            return False
            
        exists = len(data["results"]) > 0
        print(f"Medication {medication} {'exists' if exists else 'does not exist'} in FDA database")
        return exists
    except Exception as e:
        print(f"Error checking FDA database: {str(e)}")
        return False


@app.route('/api/check-interaction', methods=['POST'])
def check_interaction():
    data = request.get_json()
    med1 = data.get('medication1', '').strip()
    med2 = data.get('medication2', '').strip()
    
    if not med1 or not med2:
        return jsonify({'success': False, 'message': 'Both medications are required'})
    
    # First check if medications exist in FDA database
    med1_exists = check_if_medication_exists(med1)
    med2_exists = check_if_medication_exists(med2)
    
    if not med1_exists or not med2_exists:
        return jsonify({
            'success': False,
            'message': 'One or both medications not found in FDA database'
        })
    
    # Use LLM to analyze the interaction
    analysis = analyze_interaction(med1, med2)
    print(f"AI Analysis result: {analysis}")
    
    # Check if the analysis starts with "Error:" to indicate an error message
    if analysis and analysis.startswith("Error:"):
        return jsonify({
            'success': False,
            'message': analysis
        })
    
    if not analysis:
        return jsonify({
            'success': False,
            'message': 'Error analyzing medication interaction'
        })
    
    # Return the analysis with success status
    response = {
        'success': True,
        'message': 'Interaction analysis completed',
        'analysis': analysis
    }
    print(f"Sending response: {response}")
    return jsonify(response)


@app.route('/api/check-medication', methods=['POST'])
def check_medication():
    data = request.json
    medication = data.get('medicationName')
    
    if not medication:
        return jsonify({
            "success": False,
            "error": "Medication name is required"
        }), 400
    
    print(f"Received medication check request for: {medication}")
    result = check_name(medication)
    
    # Check if the result contains "not found" to determine if the medication exists
    exists = "not found" not in result.lower()
    
    response = {
        "success": True,
        "exists": exists,
        "message": result
    }
    
    print(f"Sending response: {response}")
    return jsonify(response)

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        user = create_user(data)
        return jsonify({"success": True, "user": user}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "An error occurred during signup"}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = verify_user(data['email'], data['password'])
        if user:
            return jsonify({"success": True, "user": user}), 200
        return jsonify({"success": False, "error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"success": False, "error": "An error occurred during login"}), 500

@app.route('/api/user/<email>', methods=['GET'])
def get_user_profile(email):
    try:
        user = get_user(email)
        if user:
            # Remove password from response
            user_copy = user.copy()
            user_copy.pop('password', None)
            return jsonify({"success": True, "user": user_copy}), 200
        return jsonify({"success": False, "error": "User not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": "An error occurred"}), 500

@app.route('/api/user/<email>', methods=['PUT'])
def update_user_profile(email):
    try:
        data = request.get_json()
        user = update_user(email, data)
        return jsonify({"success": True, "user": user}), 200
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "An error occurred"}), 500

@app.route('/api/user/<email>', methods=['DELETE'])
def delete_user_profile(email):
    try:
        if delete_user(email):
            return jsonify({"success": True}), 200
        return jsonify({"success": False, "error": "User not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)