import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import MedicationLog from './components/medication/MedicationLog';
import InteractionAnalysis from './components/medication/InteractionAnalysis';
import Layout from './components/layout/Layout';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/patient/*" element={
          <Layout>
            <Routes>
              <Route index element={<MedicationLog />} />
              <Route path="interactions" element={<InteractionAnalysis />} />
            </Routes>
          </Layout>
        } />
        <Route path="/physician/*" element={
          <Layout>
            <Routes>
              <Route index element={<MedicationLog />} />
              <Route path="interactions" element={<InteractionAnalysis />} />
            </Routes>
          </Layout>
        } />
        <Route path="/" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App; 