import React, { useState, useEffect } from 'react';
import {
  Box,
  Container,
  Typography,
  Paper,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Chip,
  Alert,
  CircularProgress,
} from '@mui/material';
import WarningIcon from '@mui/icons-material/Warning';
import InfoIcon from '@mui/icons-material/Info';
import { checkInteraction } from '../../api';
import ReactMarkdown from 'react-markdown';

const InteractionAlerts = () => {
  const [interactions, setInteractions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const analyzeInteractions = async () => {
      const savedMedications = localStorage.getItem('medications');
      if (!savedMedications) {
        setError('No medications found. Please add medications first.');
        return;
      }

      const medications = JSON.parse(savedMedications);
      if (medications.length < 2) {
        setError('Please add at least two medications to analyze interactions.');
        return;
      }

      setLoading(true);
      setError(null);
      const newInteractions = [];

      // Analyze each pair of medications
      for (let i = 0; i < medications.length; i++) {
        for (let j = i + 1; j < medications.length; j++) {
          try {
            const response = await checkInteraction(
              medications[i].medicationName,
              medications[j].medicationName
            );
            
            if (response.success && response.analysis) {
              newInteractions.push({
                id: `${i}-${j}`,
                severity: 'high',
                medications: [medications[i].medicationName, medications[j].medicationName],
                description: response.analysis,
              });
            }
          } catch (err) {
            console.error('Error checking interaction:', err);
          }
        }
      }

      setInteractions(newInteractions);
      setLoading(false);
    };

    analyzeInteractions();
  }, []);

  const getSeverityColor = (severity) => {
    switch (severity) {
      case 'high':
        return 'error';
      case 'medium':
        return 'warning';
      case 'low':
        return 'info';
      default:
        return 'default';
    }
  };

  if (loading) {
    return (
      <Container maxWidth="md">
        <Box sx={{ mt: 4, mb: 4, display: 'flex', justifyContent: 'center' }}>
          <CircularProgress />
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" component="h2" gutterBottom>
          Medication Interactions
        </Typography>

        {error && (
          <Alert severity="error" sx={{ mt: 2 }}>
            {error}
          </Alert>
        )}

        {interactions.length === 0 && !error ? (
          <Alert severity="success" sx={{ mt: 2 }}>
            No medication interactions detected.
          </Alert>
        ) : (
          <List>
            {interactions.map((interaction) => (
              <Paper
                key={interaction.id}
                elevation={2}
                sx={{ mb: 2, p: 2 }}
              >
                <ListItem alignItems="flex-start">
                  <ListItemIcon>
                    {interaction.severity === 'high' ? (
                      <WarningIcon color="error" />
                    ) : (
                      <InfoIcon color="warning" />
                    )}
                  </ListItemIcon>
                  <ListItemText
                    primary={
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
                        <Typography variant="h6" component="span">
                          Interaction Detected
                        </Typography>
                        <Chip
                          label={interaction.severity.toUpperCase()}
                          color={getSeverityColor(interaction.severity)}
                          size="small"
                        />
                      </Box>
                    }
                    secondary={
                      <>
                        <Typography
                          component="span"
                          variant="body2"
                          color="text.primary"
                          sx={{ display: 'block', mb: 1 }}
                        >
                          Medications involved: {interaction.medications.join(' + ')}
                        </Typography>
                        <Typography
                          component="span"
                          variant="body2"
                          color="text.secondary"
                          sx={{ whiteSpace: 'pre-line' }}
                        >
                          <div className="markdown-content">
                            <ReactMarkdown>{interaction.description}</ReactMarkdown>
                          </div>
                        </Typography>
                      </>
                    }
                  />
                </ListItem>
              </Paper>
            ))}
          </List>
        )}
      </Box>
    </Container>
  );
};

export default InteractionAlerts; 