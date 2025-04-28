import React, { useState, useEffect } from 'react';
import {
  Box,
  Container,
  Typography,
  Paper,
  TextField,
  Button,
  CircularProgress,
  Alert,
  List,
  ListItem,
  ListItemText,
  Divider,
} from '@mui/material';
import { checkInteraction } from '../../api';
import ReactMarkdown from 'react-markdown';

const InteractionAnalysis = () => {
  const [medication1, setMedication1] = useState('');
  const [medication2, setMedication2] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [interactionResult, setInteractionResult] = useState(null);
  const [loadingTime, setLoadingTime] = useState(0);

  useEffect(() => {
    let timer;
    if (loading) {
      timer = setInterval(() => {
        setLoadingTime(prev => prev + 1);
      }, 1000);
    } else {
      setLoadingTime(0);
    }
    return () => clearInterval(timer);
  }, [loading]);

  useEffect(() => {
    if (interactionResult) {
      console.log('Interaction result updated:', interactionResult);
      console.log('Analysis content:', interactionResult.analysis);
    }
  }, [interactionResult]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Submitting medications:', medication1, medication2);
    setLoading(true);
    setError(null);
    setInteractionResult(null);
    setLoadingTime(0);

    try {
      console.log('Calling checkInteraction API...');
      const result = await checkInteraction(medication1, medication2);
      console.log('Received interaction result:', result);
      
      if (!result) {
        console.error('No result received from API');
        setError('No response received from the server. Please try again.');
        return;
      }
      
      if (!result.success) {
        console.error('API returned success: false', result.message);
        setError(result.message || 'Failed to analyze medication interaction. Please try again.');
        return;
      }
      
      if (!result.analysis) {
        console.error('No analysis in response', result);
        setError('No analysis was returned. Please try again.');
        return;
      }
      
      console.log('Setting interaction result with analysis:', result.analysis.substring(0, 100) + '...');
      setInteractionResult(result);
    } catch (err) {
      console.error('Error in handleSubmit:', err);
      setError('Failed to check medication interaction. Please try again. Error: ' + (err.message || 'Unknown error'));
    } finally {
      setLoading(false);
    }
  };

  const getLoadingMessage = () => {
    if (loadingTime < 30) {
      return 'Analyzing medication interaction...';
    } else if (loadingTime < 60) {
      return 'Still analyzing... This may take a moment.';
    } else {
      return 'Taking longer than usual... Please be patient.';
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Medication Interaction Analysis
        </Typography>
        
        <Paper sx={{ p: 3, mb: 3 }}>
          <form onSubmit={handleSubmit}>
            <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
              <TextField
                fullWidth
                label="First Medication"
                value={medication1}
                onChange={(e) => setMedication1(e.target.value)}
                required
              />
              <TextField
                fullWidth
                label="Second Medication"
                value={medication2}
                onChange={(e) => setMedication2(e.target.value)}
                required
              />
            </Box>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={loading}
              sx={{ minWidth: 200 }}
            >
              {loading ? (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <CircularProgress size={24} color="inherit" />
                  <Typography variant="body2">{getLoadingMessage()}</Typography>
                </Box>
              ) : (
                'Check Interaction'
              )}
            </Button>
          </form>
        </Paper>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        {interactionResult && !interactionResult.success && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {interactionResult.message}
          </Alert>
        )}

        {interactionResult && interactionResult.success && (
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom color="primary">
              Interaction Analysis Results
            </Typography>
            
            <Box sx={{ 
              mt: 2, 
              '& p': { mb: 1 },
              '& ul': { ml: 2 },
              '& li': { mb: 0.5 },
              '& strong': { color: 'primary.main' }
            }}>
              {interactionResult.analysis ? (
                <div className="markdown-content">
                  <ReactMarkdown>{interactionResult.analysis}</ReactMarkdown>
                </div>
              ) : (
                <Typography color="error">
                  No analysis was returned. Please try again.
                </Typography>
              )}
            </Box>

            {interactionResult.raw_data && (
              <>
                <Divider sx={{ my: 3 }} />
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Additional Information from FDA Database:
                </Typography>
                <List>
                  {interactionResult.raw_data.map((detail, index) => (
                    <ListItem key={index}>
                      <ListItemText
                        primary={`Source: ${detail.source}`}
                        secondary={detail.details}
                      />
                    </ListItem>
                  ))}
                </List>
              </>
            )}
          </Paper>
        )}
      </Box>
    </Container>
  );
};

export default InteractionAnalysis; 