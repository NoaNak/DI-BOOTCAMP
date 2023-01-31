let user = document.getElementById("user");
user.addEventListener("keypress", world);

function world(event){
    let charCode = event.charCode
    // pour chaque lettre il y a un code, mais comme on les connais pas tous par coeur charcode les connais
    if(!(charCode >= 65 && charCode <= 90) && !(charCode >= 97 && charCode <= 122)){
        event.preventDefault();
    }
    // si je veux que des lettres c ce code specifique
}
    
