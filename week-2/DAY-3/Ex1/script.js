// remove “Greg” from the people array.
    const people = ["Greg", "Mary", "Devon", "James"];
    const index = people.indexOf("Greg");
    if (index > -1) {
        people.splice(index, 1);
}


// replace “James” to “Jason”.
// indexof c pour trouver la position
    const index1 = people.indexOf("James");
    if (index > -1) {
        people[index1] = "Jason";
    }


// Write code to add your name to the end of the people array.
    people.push("Noa");
    console.log(people); 


// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
    console.log(people.indexOf("Mary"));


// Écrivez du code pour faire une copie du peopletableau à l'aide de la sliceméthode.
    console.log(people.slice(1, 3));


// Écrivez le code qui donne l'index de "Foo". Pourquoi renvoie-t-il -1 ?
    console.log(people.indexOf("Foo"));
    // its return me to -1, bc Foo doesnt exist


// Créez une variable appelée lastdont la valeur est le dernier élément du tableau.
    const last = people[people.length -1];
    console.log(last);


// À l'aide d'une boucle, parcourez le people tableau et console.log chaque personne.
    for(let compteur = 0; compteur < people.length; compteur++) {
        console.log(people[compteur]);
    }

    for(let compteur = 0; compteur < people.length; compteur ++){
        console.log(people[compteur]);
        if (people[compteur] == "Jason") {
            break;
        }
    }