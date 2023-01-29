//acces the div 
const firstDiv = document.body.firstElementChild;
const firstDivSecondWay = document.body.children[0];

// acces the ul
const list = document.body.children[1];
const listotherWay = firstDiv.nextElementSibling; //sibling of the div accessed above

//acces li
const secondLi = list.lastElementChild; //last child of the ul accessed above;
const secondLiOtherWay = list.children[1];