//1. retrieve the form
const sphereform = document.querySelector("#Myform");

//2. add an event listener of submit on the form not on the button
sphereform.addEventListener("submit", calculateVolume);

//3. when the form is submitted this function is called
function calculateVolume(evt) {
    evt.preventDefault(); // prevent the form submission from rafraiching the page
    const inputRadiusValue = evt.target.radius.value; 
    const volumeResult = inputRadiusValue**3;
    //retrieve the value of the first inputradius
    //const volumeResult = inputRadiusVolume**3 // calculate some kind of formula
    const inputVolume = evt.target.volume;
    inputVolume.value = volumeResult;
}