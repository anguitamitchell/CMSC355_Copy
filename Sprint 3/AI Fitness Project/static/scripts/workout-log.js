document.getElementById("add-form-btn").addEventListener("click", function() {
    const formContainer = document.getElementById("workout-form"); 
    const lastFormChild = document.querySelector(".form-child"); 
    const submitButton = document.getElementById("submit-button");

    if (lastFormChild && submitButton) {
        const clonedFormChild = lastFormChild.cloneNode(true); 
        clonedFormChild.querySelectorAll("input").forEach(input => input.value = "");

        clonedFormChild.querySelector("#sets_field input").value = 1;
        clonedFormChild.querySelector("#reps_field input").value = 1;

        formContainer.insertBefore(clonedFormChild, submitButton); 

        clonedFormChild.querySelector("#delete-field").addEventListener("click", function() {
            clonedFormChild.remove(); 
        });
    }
});


