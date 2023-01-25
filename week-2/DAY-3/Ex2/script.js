// Create an array called colors where the value is a list of your five favorite colors.
    const colors = ["blue", "red", "purple", "black", "grey"];
    const number = ["st", "nd", "rd", "th"];


// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
    for(let compteur = 0; compteur < number.length; compteur ++) {
        // console.log(`My choice n°${compteur + 1} is ${colors[compteur]}`);
            console.log(`My ${compteur + 1} ${number[compteur]} choise is ${colors[compteur]}`);
}


