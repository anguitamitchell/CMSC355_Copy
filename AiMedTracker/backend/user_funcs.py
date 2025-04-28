### This file is for all the user-related functions. didn't want everything in a single file

import json
import os
import hashlib
from typing import Dict, List, Optional, Union

# Path to the users.json file
USERS_FILE = 'data/users.json'

def load_users() -> Dict:
    """Load users from the JSON file."""
    if not os.path.exists(USERS_FILE):
        return {"users": {}}
    
    try:
        with open(USERS_FILE, 'r') as f:
            data = json.load(f)
            return data if "users" in data else {"users": data}
    except (json.JSONDecodeError, FileNotFoundError):
        return {"users": {}}

def save_users(users: Dict) -> None:
    """Save users to the JSON file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def get_user(email: str) -> Optional[Dict]:
    """Get a user by email."""
    users = load_users()
    return users["users"].get(email)

def get_all_users() -> List[Dict]:
    """Get all users."""
    users = load_users()
    return list(users["users"].values())

def create_user(user_data: Dict) -> Dict:
    """Create a new user."""
    users = load_users()
    
    # Check if user already exists
    if user_data['email'] in users["users"]:
        raise ValueError("User with this email already exists")
    
    # Hash the password
    user_data['password'] = hash_password(user_data['password'])
    
    # Add user to the dictionary
    users["users"][user_data['email']] = user_data
    
    # Save to file
    save_users(users)
    
    # Return user without password
    user_copy = user_data.copy()
    user_copy.pop('password', None)
    return user_copy

def update_user(email: str, user_data: Dict) -> Dict:
    """Update an existing user."""
    users = load_users()
    
    # Check if user exists
    if email not in users["users"]:
        raise ValueError("User not found")
    
    # Update user data
    for key, value in user_data.items():
        if key == 'password' and value:
            # Hash new password if provided
            users["users"][email][key] = hash_password(value)
        elif key != 'email':  # Don't allow email changes
            users["users"][email][key] = value
    
    # Save to file
    save_users(users)
    
    # Return updated user without password
    user_copy = users["users"][email].copy()
    user_copy.pop('password', None)
    return user_copy

def delete_user(email: str) -> bool:
    """Delete a user."""
    users = load_users()
    
    # Check if user exists
    if email not in users["users"]:
        return False
    
    # Remove user
    del users["users"][email]
    
    # Save to file
    save_users(users)
    return True

def verify_user(email: str, password: str) -> Optional[Dict]:
    """Verify user credentials."""
    users = load_users()
    
    # Check if user exists
    if email not in users["users"]:
        return None
    
    # Verify password
    if users["users"][email]['password'] != hash_password(password):
        return None
    
    # Return user without password
    user_copy = users["users"][email].copy()
    user_copy.pop('password', None)
    return user_copy
