alert("Hello");

const nextBtn = document.querySelectorAll('form .next-btn');
const prevBtn = document.querySelectorAll('form .prev-btn');
// const form = document.querySelector('form');
const progress = document.getElementById("progress");
// Create arrays of all form steps to cycle through.
const steps = Array.from(document.querySelectorAll('form .step'));
const pbsteps = document.querySelectorAll('.pbstep');

let stepIdx = 0;

// Add event listeners to next buttons
nextBtn.forEach(button => {
    button.addEventListener('click', (e) => {
        changeStep('next');
        updateProgressBar();
    });
})

// Add event listeners to prev buttons
prevBtn.forEach(button => {
    button.addEventListener('click', (e) => {
        changeStep('prev');
        updateProgressBar();
    });
})

// changeStep function handles changing form sections when a button is clicked.
function changeStep(btn) {
    // get index of current active step and remove active class.
    const active = document.querySelector('form .step.active');
    stepIdx = steps.indexOf(active);
    steps[stepIdx].classList.remove('active');

    // Depending on which button is pressed, increment or decrement stepIdx.
    if (btn === 'next') {
        // if next button clicked, increment stepIdx
        stepIdx ++;
    } else if (btn === 'prev') {
        // if prev button clicked, decrement stepIdx
        stepIdx --;
    }

    // apply active class to current form step.
    steps[stepIdx].classList.add('active');
}

function updateProgressBar() {
    pbsteps.forEach((pbstep, pbstepIdx) => {
        console.log(pbstep, pbstepIdx);
        // +1 because will need to highlight the current step even though not completed.
        if (pbstepIdx < stepIdx + 1) {
            pbstep.classList.add('pbstep-active');
        } else {
            pbstep.classList.remove('pbstep-active');
        }
    });

    // Update progress bar line
    const activeSteps = document.querySelectorAll(".pbstep-active");
    progress.style.width = ((activeSteps.length - 1) / (pbsteps.length - 1)) * 75 + "%";
}


// form.addEventListener('submit', (e) => {
//     // e.preventDefault();
//     const inputs = [];
//     form.querySelectorAll('input').forEach(input => {
//         const {name, value} = input;
//         inputs.push({name, value});
//     });
//     console.log(inputs);
// })
