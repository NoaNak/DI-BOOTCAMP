// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

setTimeout(Hello, 2000); 

function Hello () {
    alert('Hello World');
    const paragraph = document.createElement("p");
    const text = document.createTextNode('Hello World');
    paragraph.appendChild(text);

    const container = document.getElementById('container');
    container.appendChild(paragraph);
    //append child rajouter le container dasn le paragraph
}

let counter = 0;

const repeat = setInterval(newPara, 2000);


// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

function newPara() {
    const paragraphTwo = document.createElement("p2");
    const text = document.createTextNode('Hello World 2');
    paragraphTwo.appendChild(text);

    const container = document.getElementById('container');
    container.appendChild(paragraphTwo);

    counter ++;
    if(counter === 5) {
        clearInterval(repeat);
    } 
}

document.getElementById('clear').addEventListener("click", function(){
    clearInterval(repeat);
});








