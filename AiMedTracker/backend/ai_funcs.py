# ai code - openrouter

import requests
import json
import os
import traceback
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_llm_response(prompt, model="openai/gpt-3.5-turbo"):
    """
    Generate a response using the OpenRouter API.
    
    Args:
        prompt (str): The input prompt for the LLM
        model (str): The model to use (default: openai/gpt-3.5-turbo)
        
    Returns:
        str: The generated response
    """
    if not OPENROUTER_API_KEY:
        print("Error: OPENROUTER_API_KEY environment variable not set")
        return "Error: API key not configured. Please contact support."
        
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://github.com/your-username/AiInteractionApp",
        "X-Title": "AI Drug Interaction App",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant that provides information about drug interactions and medications."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000,
        "timeout": 120
    }
    
    try:
        print(f"Sending prompt to OpenRouter API: {prompt[:200]}...")
        print(f"Using model: {model}")
        
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=data,
            timeout=120
        )
        
        if response.status_code != 200:
            error_msg = f"API Error: {response.status_code} - {response.text}"
            print(error_msg)
            return f"Error analyzing interaction: {error_msg}"
            
        response_json = response.json()
        
        if "choices" not in response_json or not response_json["choices"]:
            print("No choices in response")
            return "Error: No response from AI model. Please try again."
            
        result = response_json["choices"][0]["message"]["content"]
        print(f"Received response from OpenRouter API: {result[:200]}...")
        return result
        
    except requests.exceptions.Timeout:
        print("Request timed out after 120 seconds")
        return "Error: The AI model is taking longer than expected to respond. Please try again in a few moments."
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return f"Error: Could not connect to AI service. Please try again."
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(f"Full traceback: {traceback.format_exc()}")
        return "Error: An unexpected error occurred. Please try again."

def analyze_interaction(med1, med2):
    """
    Use LLM to analyze potential interactions between two medications.
    
    Args:
        med1 (str): First medication name
        med2 (str): Second medication name
        
    Returns:
        str: Analysis of potential interactions
    """
    prompt = f"""Analyze the potential interactions between {med1} and {med2}.
    
    Consider:
    1. Common side effects when taken together
    2. Potential drug interactions and their severity
    3. Contraindications or warnings
    4. Recommendations for patients taking both medications
    
    Provide a concise, patient-friendly summary that explains:
    - The main interaction concern
    - Key warnings or precautions
    - What patients should do if they're taking both medications
    
    Format the response in a clear, easy-to-read manner with bullet points where appropriate.
    Keep the response brief but informative."""
    
    return generate_llm_response(prompt)

def get_medication_info(medication):
    """
    Use LLM to get detailed information about a medication.
    
    Args:
        medication (str): Medication name
        
    Returns:
        str: Detailed information about the medication
    """
    prompt = f"""Provide detailed information about {medication}.
    Include:
    1. Common uses
    2. Typical dosage
    3. Common side effects
    4. Important warnings
    5. Drug interactions
    
    Format the response in a clear, easy-to-read manner."""
    
    return generate_llm_response(prompt)

