import React, { useState, useEffect } from 'react';
import {
  Box,
  Container,
  TextField,
  Button,
  Typography,
  Paper,
  Grid,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  CircularProgress,
} from '@mui/material';
import { Delete as DeleteIcon, Edit as EditIcon } from '@mui/icons-material';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { toast } from 'react-toastify';
import { checkMedication } from '../../api';

const STORAGE_KEY = 'medications';

const validationSchema = yup.object({
  medicationName: yup.string().required('Medication name is required'),
});

const MedicationLog = () => {
  const [medications, setMedications] = useState(() => {
    // Initialize from localStorage
    const savedMedications = localStorage.getItem(STORAGE_KEY);
    return savedMedications ? JSON.parse(savedMedications) : [];
  });
  const [openDialog, setOpenDialog] = useState(false);
  const [editingMedication, setEditingMedication] = useState(null);
  const [isChecking, setIsChecking] = useState(false);

  // Save to localStorage whenever medications change
  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(medications));
  }, [medications]);

  const formik = useFormik({
    initialValues: {
      medicationName: '',
    },
    validationSchema: validationSchema,
    onSubmit: async (values, { resetForm }) => {
      if (editingMedication !== null) {
        // Update existing medication
        const updatedMedications = medications.map((med) =>
          med.id === editingMedication.id ? { ...values, id: med.id } : med
        );
        setMedications(updatedMedications);
        toast.success('Medication updated successfully!');
        handleCloseDialog();
        resetForm();
      } else {
        // Check for duplicate medication
        const isDuplicate = medications.some(
          med => med.medicationName.toLowerCase() === values.medicationName.toLowerCase()
        );
        
        if (isDuplicate) {
          toast.error('This medication is already in your list');
          return;
        }

        // Check if medication exists in FDA database
        setIsChecking(true);
        try {
          console.log('Submitting medication:', values.medicationName);
          const response = await checkMedication(values.medicationName);
          console.log('Received response:', response);
          
          if (response.success) {
            if (response.exists) {
              // Add new medication
              const newMedication = {
                ...values,
                id: Date.now(),
              };
              setMedications([...medications, newMedication]);
              toast.success('Medication added successfully!');
              handleCloseDialog();
              resetForm();
            } else {
              toast.error(response.message || 'Medication not found in FDA database');
            }
          } else {
            toast.error(response.error || 'Failed to check medication');
          }
        } catch (err) {
          console.error('Error in form submission:', err);
          toast.error(err.message || 'An error occurred while checking the medication');
        } finally {
          setIsChecking(false);
        }
      }
    },
  });

  const handleOpenDialog = (medication = null) => {
    if (medication) {
      setEditingMedication(medication);
      formik.setValues(medication);
    } else {
      setEditingMedication(null);
      formik.resetForm();
    }
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
    setEditingMedication(null);
    formik.resetForm();
  };

  const handleDeleteMedication = (id) => {
    setMedications(medications.filter((med) => med.id !== id));
    
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Medication Log
        </Typography>
        
        <Button
          variant="contained"
          color="primary"
          onClick={() => handleOpenDialog()}
          sx={{ mb: 3 }}
        >
          Add New Medication
        </Button>

        <Paper elevation={3}>
          <List>
            {medications.map((medication) => (
              <ListItem key={medication.id} divider>
                <ListItemText
                  primary={medication.medicationName}
                />
                <ListItemSecondaryAction>
                  <IconButton
                    edge="end"
                    aria-label="edit"
                    onClick={() => handleOpenDialog(medication)}
                    sx={{ mr: 1 }}
                  >
                    <EditIcon />
                  </IconButton>
                  <IconButton
                    edge="end"
                    aria-label="delete"
                    onClick={() => handleDeleteMedication(medication.id)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </ListItemSecondaryAction>
              </ListItem>
            ))}
          </List>
        </Paper>

        <Dialog open={openDialog} onClose={handleCloseDialog}>
          <DialogTitle>
            {editingMedication ? 'Edit Medication' : 'Add New Medication'}
          </DialogTitle>
          <form onSubmit={formik.handleSubmit}>
            <DialogContent>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    id="medicationName"
                    name="medicationName"
                    label="Medication Name"
                    value={formik.values.medicationName}
                    onChange={formik.handleChange}
                    error={formik.touched.medicationName && Boolean(formik.errors.medicationName)}
                    helperText={formik.touched.medicationName && formik.errors.medicationName}
                    disabled={isChecking}
                  />
                </Grid>
              </Grid>
            </DialogContent>
            <DialogActions>
              <Button onClick={handleCloseDialog} disabled={isChecking}>Cancel</Button>
              <Button 
                type="submit" 
                variant="contained" 
                color="primary"
                disabled={isChecking}
              >
                {isChecking ? (
                  <CircularProgress size={24} color="inherit" />
                ) : (
                  editingMedication ? 'Update' : 'Add'
                )}
              </Button>
            </DialogActions>
          </form>
        </Dialog>
      </Box>
    </Container>
  );
};

export default MedicationLog; 