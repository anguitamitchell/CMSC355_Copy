import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { storeUser } from './utils/auth'

// Initialize test users if none exist
const initializeTestUsers = () => {
  const testUsers = {
    'patient@test.com': {
      email: 'patient@test.com',
      password: 'password123',
      type: 'patient',
      firstName: 'Test',
      lastName: 'Patient'
    },
    'doctor@test.com': {
      email: 'doctor@test.com',
      password: 'password123',
      type: 'physician',
      firstName: 'Test',
      lastName: 'Doctor'
    }
  };

  // Only initialize if no users exist
  if (!localStorage.getItem('users')) {
    Object.values(testUsers).forEach(user => storeUser(user));
  }
};

// Initialize test users
initializeTestUsers();

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
