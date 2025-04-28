// Function to get all stored users from localStorage
export const getStoredUsers = () => {
  const users = localStorage.getItem('users');
  return users ? JSON.parse(users) : {};
};

// Function to store a new user
export const storeUser = (userData) => {
  const users = getStoredUsers();
  users[userData.email] = userData;
  localStorage.setItem('users', JSON.stringify(users));
};

// Function to update user data
export const updateStoredUser = (email, updates) => {
  const users = getStoredUsers();
  if (users[email]) {
    users[email] = { ...users[email], ...updates };
    localStorage.setItem('users', JSON.stringify(users));
  }
};

// Function to get a specific user
export const getStoredUser = (email) => {
  const users = getStoredUsers();
  return users[email] || null;
}; 