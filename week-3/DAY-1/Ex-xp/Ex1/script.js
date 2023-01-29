// Récupérez le div et console.log it
const firstDiv = document.getElementById("container");
console.log(firstDiv);

// Changez le nom "Pete" en "Richard".
const firstUl = document.body.children[1];
const secondLi = firstUl.lastElementChild;
secondLi.textContent = "Richard";
console.log(firstUl);

// Remplacez chaque prénom des deux <ul>'s par votre nom.
const allUL = document.getElementsByClassName("list");
for(let ul of allUL){
    ul.firstElementChild.textContent = "Noa";
}
console.log(allUL);

// Supprimez le <li>qui contient le nœud de texte "Sarah".
const secondUl = document.body.children[2]
secondUl.children[1].remove();




