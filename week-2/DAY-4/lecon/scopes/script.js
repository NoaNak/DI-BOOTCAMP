// SCOPES
// global
// local



// global  outside

// local 
    // function
    // loop
    // if statement

// ----------------
// WHATEVER IS DECLARED IN THE GLOBAL SCOPE, IS ACCESSIBLE IN THE LOCAL SCOPE

let user = 'John'; //GLOBAL VARIABLE
//Global variable can used in the global scoped and in the local scope

//local scope
function sayHello () { //3
    const sentence = `Welcome ${username}`;
    console.log(sentence); //Welcome John
}

//---------------

let username = 'John'; //GLOBAL VARIABLE
//Global variable can used in the global scoped and in the local scope

//local scope
function sayHello () { //3
    username = "Tom"; //redifining the username variable, redefine the global variable
    const sentence = `Welcome ${username}`;
    console.log(sentence); //Welcome Tom
}

console.log(username); //"John" //1

sayHello(); //2

console.log(username); //4 //"Tom"

// --------------- LOCAL SCOPE -------------------
// WHATEVER IS DECLARED IN THE LOCAL SCOPE, IS NOT ACCESSIBLE IN THE GLOBAL SCOPE

//local scope
function getSum () {
    const sum = 2+3; //DECLARED IN THE FUNCTION // SO ITS A LOCAL VARIABLE
    console.log(sum);
}

getSum()

//global scope
console.log(sum); //sum is not defined

// LOCAL SCOPE AND BLOCK SCOPE ARE "PRIVATE" --> cannot access them outside the block
function test () {
    if (true) {
        const user = "John";
    }
    const sentence = `Hello ${user}`; //error
}

// GLOBAL

// LOCAL
//  - FUNCTION SCOPE
//  - BLOCK SCOPE - IF, FOR, SWITCH, WHILE

for (let i = 0; i<= 2; i++){
    console.log(i);
}

const sentence = `${i} is my number`; //i is not defined