// i do all this wth internet bc im not understand 

myElement.addEventListener("click", function(){
    x += 10;
    y += 10;
    myElement.style.left = x + "px";
    myElement.style.top = y + "px";
});
myElement.addEventListener("mouseover", function(){
    size += 5;
    myElement.style.fontSize = size + "px";
});
myElement.addEventListener("mouseout", function(){
    color = (color == "blue") ? "red" : "blue";
    myElement.style.backgroundColor = color;
});
myElement.addEventListener("dblclick", function(){
    size = 16;
    x = 50;
    y = 50;
    color = "blue";
    myElement.style.left = x + "px";
    myElement.style.top = y + "px";
    myElement.style.backgroundColor = color;
    myElement.style.fontSize = size + "px";
});