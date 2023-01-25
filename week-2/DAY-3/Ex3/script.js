// Demander à l'utilisateur un numéro.
// Astuce : Vérifiez le type de données que vous recevez à partir de l'invite (c.-à-d. Utilisez la typeofméthode)

// Tant que le nombre est inférieur à 10, continuez à demander à l'utilisateur un nouveau numéro.
// Astuce : Quelle whileboucle est la plus pertinente pour cette situation ?

let num = prompt("Give me a number");
num = Number(num);
while(num < 10) {
     num = prompt("Give me a number");
}
