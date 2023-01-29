// Add a “light blue” background color and some padding to the <div>.
const div = document.body.firstElementChild.style.backgroundColor = "lightblue";
const padding = document.body.firstElementChild.style.padding = "2em";

// Do not display the <li> that contains the text node “John”.
const myUl = document.body.children[1]
myUl.children[0].remove();

// Add a border to the <li> that contains the text node “Pete”.
myUl.children[0].style.border = "2px solid black";

// Change the font size of the whole body.
document.body.style.fontSize = "15px";

if (document.body.firstElementChild.style.backgroundColor === "lightblue"){
    alert("hey x and y");
}