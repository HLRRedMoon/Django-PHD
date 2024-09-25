
// function updateBullets(currentStep) {
//     const bullets = document.querySelectorAll('.bullet');
//     const leftArrow = document.querySelector('.left-arrow');
//     const rightArrow = document.querySelector('.right-arrow');
//     const maxSteps = 4; // Assuming there are 4 steps

//     bullets.forEach((bullet, index) => {
//         if (index < currentStep - 1) {
//             bullet.classList.add('completed');
//         } else {
//             bullet.classList.remove('completed');
//         }
//         if (index === currentStep - 1) {
//             bullet.classList.add('current');
//         } else {
//             bullet.classList.remove('current');
//         }
//     });

//     // Update arrow visibility
//     leftArrow.style.display = (currentStep === 1) ? 'none' : 'inline';
//     rightArrow.style.display = (currentStep === maxSteps) ? 'none' : 'inline';
// }
// document.addEventListener('DOMContentLoaded', function() {
//     updateBullets(1); // Assuming the first step is displayed on load
// });

// function nextStep(step) {
//     document.getElementById('step' + (step - 1)).className = "step hidden";
//     document.getElementById('step' + step).className = "step ";
//     updateBullets(step);
// }

// function previousStep(step) {
//     document.getElementById('step' + (step + 1)).className = "step hidden";
//     document.getElementById('step' + step).className = "step ";
//     updateBullets(step);
// }

// function navigateLeft() {
//     const currentStepIndex = getCurrentStepIndex();
//     if (currentStepIndex > 0) {
//         previousStep(currentStepIndex);
//     }
// }

// function navigateRight() {
//     const currentStepIndex = getCurrentStepIndex();
//     const maxSteps = 4; // Assuming there are 4 steps, adjust this number based on your actual steps
//     if (currentStepIndex < maxSteps) {
//         nextStep(currentStepIndex + 2); // +2 because nextStep function expects the next step number, not index
//     }
// }

// function getCurrentStepIndex() {
//     const steps = document.querySelectorAll('.step');
//     let currentIndex = 0;
//     steps.forEach((step, index) => {
//         if (!step.classList.contains('hidden')) {
//             currentIndex = index;
//         }
//     });
//     return currentIndex;
// }

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('.inp-date, .chi-rad, .inp-num, .inp-sel');
    const errorDisplay = document.getElementById('errorDisplay'); // Get the existing error display element

    function validateForm(event) {
        let isValid = true;
        let firstInvalidInput = null;

        inputs.forEach(input => {
            if (input.type === 'radio') {
                const name = input.name;
                const radioGroup = document.querySelectorAll(`input[name="${name}"]`);
                const checked = [...radioGroup].some(radio => radio.checked);
                if (!checked && !firstInvalidInput) {
                    isValid = false;
                    firstInvalidInput = input; // Capture the first invalid input for focusing later
                }
            } else if (!input.value.trim()) {
                isValid = false;
                input.style.borderColor = 'red'; // Highlight empty fields
                firstInvalidInput = firstInvalidInput || input;
            } else {
                input.style.borderColor = ''; // Reset border color if valid
            }
        });

        if (!isValid) {
            errorDisplay.textContent = 'Please fill out all required fields.';
            errorDisplay.className = 'block'; // Make sure the error display is visible
            event.preventDefault(); // Prevent form submission
            firstInvalidInput.focus(); // Focus the first invalid input
        } else {
            errorDisplay.textContent = '';
            errorDisplay.style.display = 'none'; // Hide the error display
        }
    }

    form.addEventListener('submit', validateForm);
});

document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll('.inp-date, .inp-num, .inp-sel, .chi-rad');

    inputs.forEach(input => {
        // Handle input or change events
        input.addEventListener('input', function() {
            const star = this.parentNode.querySelector('.red'); // Assuming the '.red' span is a direct sibling
            if (this.value.trim() !== '') {
                star.style.display = 'none'; // Hide star if input is not empty
            } else {
                star.style.display = 'inline'; // Show star if input is empty
            }
        });

        if (input.type === 'radio') {
            // Handle radio buttons separately since they're not 'empty' in the traditional sense
            const radios = document.querySelectorAll(`input[name="${input.name}"]`);
            radios.forEach(radio => {
                radio.addEventListener('change', function() {
                    const star = this.closest('li').querySelector('.red');
                    if (this.checked) {
                        star.style.display = 'none'; // Hide star when any radio is selected
                    }
                });
            });
        }
    });
});


function updateBullets(currentStep, steps) {
    const bullets = document.querySelectorAll('.bullet');
    const leftArrow = document.querySelector('.left-arrow');
    const rightArrow = document.querySelector('.right-arrow');
    const maxSteps = steps.length;

    bullets.forEach((bullet, index) => {
        if (index < currentStep - 1) {
            bullet.classList.add('completed');
        } else {
            bullet.classList.remove('completed');
        }
        if (index === currentStep - 1) {
            bullet.classList.add('current');
        } else {
            bullet.classList.remove('current');
        }
    });

    leftArrow.style.display = (currentStep === 1) ? 'none' : 'inline';
    rightArrow.style.display = (currentStep === maxSteps) ? 'none' : 'inline';
}

document.addEventListener('DOMContentLoaded', function() {
    const steps = document.querySelectorAll('.step');
    updateBullets(1, steps);
});

function nextStep(step) {
    const steps = document.querySelectorAll('.step');
    if (step > 0 && step < steps.length) {
        steps[step - 1].classList.add('hidden');
        steps[step].classList.remove('hidden');
        updateBullets(step + 1, steps);
    }
}

function previousStep(step) {
    const steps = document.querySelectorAll('.step');
    if (step > 0 && step < steps.length) {
        steps[step].classList.add('hidden');
        steps[step - 1].classList.remove('hidden');
        updateBullets(step, steps);
    }
}

function navigateLeft() {
    const currentStepIndex = getCurrentStepIndex();
    if (currentStepIndex > 0) {
        previousStep(currentStepIndex);
    }
}

function navigateRight() {
    const currentStepIndex = getCurrentStepIndex();
    const steps = document.querySelectorAll('.step');
    if (currentStepIndex < steps.length - 1) {
        nextStep(currentStepIndex + 1);
    }
}

function getCurrentStepIndex() {
    const steps = document.querySelectorAll('.step');
    let currentIndex = 0;
    steps.forEach((step, index) => {
        if (!step.classList.contains('hidden')) {
            currentIndex = index;
        }
    });
    return currentIndex;
}

// document.addEventListener("DOMContentLoaded", function() {
//     const form = document.querySelector('form');
//     const inputs = document.querySelectorAll('.inp-date, .chi-rad, .inp-num, .inp-sel');
//     const errorDisplay = document.getElementById('errorDisplay');

//     function validateForm(event) {
//         let isValid = true;
//         let firstInvalidInput = null;

//         inputs.forEach(input => {
//             if (input.type === 'radio') {
//                 const name = input.name;
//                 const radioGroup = document.querySelectorAll(`input[name="${name}"]`);
//                 const checked = [...radioGroup].some(radio => radio.checked);
//                 if (!checked && !firstInvalidInput) {
//                     isValid = false;
//                     firstInvalidInput = input;
//                 }
//             } else if (!input.value.trim()) {
//                 isValid = false;
//                 input.style.borderColor = 'red';
//                 firstInvalidInput = firstInvalidInput || input;
//             } else {
//                 input.style.borderColor = '';
//             }
//         });

//         if (!isValid) {
//             errorDisplay.textContent = 'Please fill out all required fields.';
//             errorDisplay.classList.remove('hidden');
//             event.preventDefault();
//             firstInvalidInput.focus();
//         } else {
//             errorDisplay.textContent = '';
//             errorDisplay.classList.add('hidden');
//         }
//     }

//     form.addEventListener('submit', validateForm);
// });

