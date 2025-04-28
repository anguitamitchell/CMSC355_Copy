const API_BASE_URL = 'http://127.0.0.1:5001/api';

export const login = async (email, password) => {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });
  const data = await response.json();
  if (!data.success) {
    throw new Error(data.error);
  }
  return data.user;
};

export const signup = async (userData) => {
  const response = await fetch(`${API_BASE_URL}/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });
  const data = await response.json();
  if (!data.success) {
    throw new Error(data.error);
  }
  return data.user;
};

export const getUserProfile = async (email) => {
  const response = await fetch(`${API_BASE_URL}/user/${email}`);
  const data = await response.json();
  if (!data.success) {
    throw new Error(data.error);
  }
  return data.user;
};

export const updateUserProfile = async (email, userData) => {
  const response = await fetch(`${API_BASE_URL}/user/${email}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });
  const data = await response.json();
  if (!data.success) {
    throw new Error(data.error);
  }
  return data.user;
};

export const deleteUserProfile = async (email) => {
  const response = await fetch(`${API_BASE_URL}/user/${email}`, {
    method: 'DELETE',
  });
  const data = await response.json();
  if (!data.success) {
    throw new Error(data.error);
  }
  return true;
};

export const checkInteraction = async (medication1, medication2) => {
  try {
    console.log('Checking interaction between:', medication1, 'and', medication2);
    const response = await fetch(`${API_BASE_URL}/check-interaction`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ medication1, medication2 }),
    });
    
    if (!response.ok) {
      console.error('API response not OK:', response.status, response.statusText);
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    
    const data = await response.json();
    console.log('Interaction check response:', data);
    return data;
  } catch (error) {
    console.error('Error in checkInteraction:', error);
    throw error;
  }
};

export const checkMedication = async (medicationName) => {
  try {
    console.log('Checking medication:', medicationName);
    const response = await fetch(`${API_BASE_URL}/check-medication`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ medicationName }),
    });
    
    if (!response.ok) {
      console.error('API response not OK:', response.status, response.statusText);
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    
    const data = await response.json();
    console.log('API response:', data);
    return data;
  } catch (error) {
    console.error('Error in checkMedication:', error);
    throw error;
  }
};