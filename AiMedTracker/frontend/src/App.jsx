import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Components
import Layout from './components/layout/Layout.jsx';
import Login from './components/auth/Login.jsx';
import SignUp from './components/auth/SignUp.jsx';
import Profile from './components/auth/Profile.jsx';
import MedicationLog from './components/medication/MedicationLog.jsx';
import InteractionAlerts from './components/medication/InteractionAlerts.jsx';
import { AuthProvider, useAuth } from './context/AuthContext.jsx';

// Create a theme instance
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

const PrivateRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <AuthProvider>
        <Router>
          <ToastContainer position="top-right" />
          <Routes>
            {/* Public Routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            
            {/* Protected Routes */}
            <Route
              path="/"
              element={
                <PrivateRoute>
                  <Layout>
                    <Navigate to="/dashboard" replace />
                  </Layout>
                </PrivateRoute>
              }
            />
            <Route
              path="/dashboard"
              element={
                <PrivateRoute>
                  <Layout>
                    <MedicationLog />
                  </Layout>
                </PrivateRoute>
              }
            />
            <Route
              path="/medications"
              element={
                <PrivateRoute>
                  <Layout>
                    <MedicationLog />
                  </Layout>
                </PrivateRoute>
              }
            />
            <Route
              path="/interactions"
              element={
                <PrivateRoute>
                  <Layout>
                    <InteractionAlerts medications={[]} />
                  </Layout>
                </PrivateRoute>
              }
            />
            <Route
              path="/profile"
              element={
                <PrivateRoute>
                  <Layout>
                    <Profile />
                  </Layout>
                </PrivateRoute>
              }
            />
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
