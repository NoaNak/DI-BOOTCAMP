function createGrid(){
    let colors = ["red", "orange", "yellow", "yellowgreen", "lightgreen", "green", "turquoise", "cyan", "lightskyblue", "dodgerblue", "blue", "purple"];

    const section = document.getElementById("sidebar");
    for(let color of colors){
        let div = document.createElement("div");
        div.setAttribute("id", "color");
        div.style.backgroundColor = color;
        div.style.width = "57px";
        div.style.height = "91px";
        div.style.marginTop = "10px";
        section.appendChild(div);
        div.addEventListener("click", retrieveColor);
        div.addEventListener("mouseover", coloring);
        div.addEventListener("mouseup", checkMouseUp);
        div.addEventListener("mousedown", checkMouseDown);
    }
    
    const paletGrill = document.getElementById("nothing");
        for(let i = 0; i < 24*60; i++){
            let div = document.createElement("div");
            div.classList.add("grid");
            // pour ajouter une classe dans mon css 
            div.style.width = "20px";
            div.style.height = "20px";
            paletGrill.appendChild(div);
            div.addEventListener("click", addColor);
    }    
}
createGrid();

let cub = document.getElementsByClassName("grid");
console.log(cub);

const button = document.querySelector('button');
    button.addEventListener('click', function(){
        for(let div of cub){
            div.style.backgroundColor = "white";
        }
    })

let color;
function retrieveColor(evt){
    color = evt.target.style.backgroundColor;
    console.log(color);
}

function addColor (evt){
    evt.target.style.backgroundColor = color;
    
    }

function coloring (evt){
    console.log(evt);
    if(isMouseDown == true) {
        console.log("test");
    evt.target.style.backgroundColor = color
    }
}

function checkMouseDown(){
    isMouseDown = true;
    //quand je click sur la couleur = true
}
let isMouseDown = false;

function checkMouseUp(){
    isMouseDown = false;
}

