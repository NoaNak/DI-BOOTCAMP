// Using a DOM property, retrieve the h1 and console.log it.
const firsth1 = document.querySelector('h1');
console.log(firsth1.textContent);

//Using DOM methods, remove the last paragraph in the <article> tag.
const lastP = document.querySelector('article');
const paragraph = lastP.lastElementChild;
paragraph.remove();

//Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
const h2 = document.querySelector("h2");
h2.addEventListener("click", background ());
function background (){
    h2.style.backgroundColor = "red";
}

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
const button = document.querySelector("#allParagraph");
button.addEventListener("click", bold);
function bold() {
    const p = document.querySelectorAll("p")
    for(let paragraph of p){
    paragraph.style.fontWeight = "bold";
    }
}
