function toggleWorkoutForm() {
    const form = document.getElementById('workout-form');
    form.style.display = (form.style.display === 'none' || form.style.display === '') ? 'block' : 'none';
}

function toggleCardioForm() {
    const form = document.getElementById('cardio-form');
    form.style.display = (form.style.display === 'none' || form.style.display === '') ? 'block' : 'none';
}