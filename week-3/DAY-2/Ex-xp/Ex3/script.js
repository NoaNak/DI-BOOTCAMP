// Declare a global variable named allBoldItems.
let allBoldItems;

// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
function getBold_items(){
    allBoldItems = document.querySelectorAll("p strong");
}
getBold_items();

// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight(){
    for(let bold of allBoldItems){
        const git = bold.style.color = "blue";
        console.log(git);
    }
}
highlight();

// Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal(){
    for(let ret of allBoldItems){
        const git2 = ret.style.color = "black";
        console.log(git2);
    }
}
return_normal();

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph).
document.querySelector("p").addEventListener("mouseover", highlight);
document.querySelector("p").addEventListener("mouseout", return_normal);