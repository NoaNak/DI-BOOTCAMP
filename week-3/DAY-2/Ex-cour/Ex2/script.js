// EX2:
// using the event object
// const colors = ["blue", "yellow", "green", "pink"];
// Add inside the HTML file a div of id "container" (do it directly in the HTML)
// Using a loop, add one button per color inside the div container (do it directly in the JS)
// Each button should have an "click" event listener that changes the background color of the document, to the color of the button (do it directly in the JS)

const colors = ["blue", "yellow", "green", "pink"];
// add the buttons of the page
function addButtons () {
    const divContainer = document.getElementById("#container");
    // loop throught all the colors with a for of loop 
    for (let color of colors) {
        // for each color

        // 1. create a button 
        const button = document.createElement("button");
        // 2. create a text content
        const content = document.createTextNode(`Click here to change to ${`color`}`)
        //3. add a value attribute equal to the color
        button.setAttribute = ("value", color);
        //4. add the text content to the button
        button.appendChild = (content);
        //5. add each button to the container
        divContainer.appendChild = (button);
        //6. for every button, I want to make it clickable
        //when the button is clicked, we call the function changeColor        
        button.addEventListener("click", changeColor);
    }
}

addButtons()

//function changeColor
function changeColor(evt) {
    console.log(evt);
    // changes the background body depending on the value attribute
    // or the button that was click (ie. evt.target)
    document.body.style.backgroundColor = evt.target.value;
}