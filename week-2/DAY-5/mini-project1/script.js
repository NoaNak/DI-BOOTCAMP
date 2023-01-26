function playTheGame(){
    let answer = confirm("Would you like to play the game?");
    if (answer === null){
        alert ("No problem, Goodbye.");
    } else {
        question1();
    }
}

function question1(){
    let question = parseInt(prompt("Pleas, unter a number between 0 and 10:"));
    if(isNaN(question)) {
        alert("Sorry it’s not a good number, Goodbye");
    } else {
        let computerNumber = Math.round(Math.random() * 11);
        compareNumbers(question, computerNumber, 3);
    }
}


function compareNumbers(userNumber, computerNumber, chances){
    while (chances > 0){
        if (userNumber === computerNumber) {
            alert("WINNER");
            break;
        } else if (userNumber > computerNumber) { 
            alert("Your number is bigger then the computer’s, guess again !");
            console.log(chances);
        } else if (userNumber < computerNumber){
            alert("Your number is smaller then the computer, give me a new number !");
            console.log(chances);
        } 
        chances--;
        if (chances === 0){
            alert("Game Over you tried 3 times");
        }

    }
}
            
            
        
    