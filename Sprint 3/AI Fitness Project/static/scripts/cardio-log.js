document.getElementById("add-form-btn").addEventListener("click", function() {
    const formContainer = document.getElementById("cardio-form"); 
    const lastFormChild = document.querySelector(".form-child"); 
    const submitButton = document.getElementById("submit-button");

    if (lastFormChild && submitButton) {
        const clonedFormChild = lastFormChild.cloneNode(true); 
        clonedFormChild.querySelectorAll("input").forEach(input => input.value = "");

        let distance = 0;

        clonedFormChild.querySelector("#distance_field input").value = distance.toFixed(2);
        clonedFormChild.querySelector("#minute_field input").value = 0;
        clonedFormChild.querySelector("#second_field input").value = 0;

        formContainer.insertBefore(clonedFormChild, submitButton); 

        clonedFormChild.querySelector("#delete-field").addEventListener("click", function() {
            clonedFormChild.remove(); 
        });
    }
});


