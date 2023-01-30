// EX1:
// basic addEventListener
// Create two buttons - id of "red", id of "blue"
// When we click on the red button -> Change the backgroundcolor of the page to red
// When we click on the blue button -> Change the backgroundcolor of the page to blue

const button = document.querySelector("#btn");
const buttonTwo = document.querySelector("#btn2");

button.addEventListener("click", changeToRed);
buttonTwo.addEventListener("click", changeToBlue);

function changeToRed() {
    document.body.style.backgroundColor = "red";
}

function changeToBlue() {
    document.body.style.backgroundColor = "blue";
}

