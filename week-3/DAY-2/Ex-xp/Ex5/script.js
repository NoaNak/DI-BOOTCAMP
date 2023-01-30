// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
const h1 = document.body.firstElementChild;
const p = document.getElementById("p");
const button =  document.getElementById("btn");

h1.addEventListener("click", hello());
p.addEventListener("mouseover", fine());
btn.addEventListener("mouseout", Goodbye());

// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.
function hello() {
    document.body.style.backgroundColor = "grey";
}

function fine() {
    p1.style.fontSize = "x-large";
}

function Goodbye() {
    btn.style.borderImage = "url(picture.png) 20 round";
}