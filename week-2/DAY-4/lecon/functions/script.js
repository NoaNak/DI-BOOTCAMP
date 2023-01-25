// SYNTAX
// function funcName (parameters) {
//     //statement
// }

// INVOKE
// funcName()


//DECLARING THE FUNCTION
// hold some program that I call as many times as I want
function sayHello () {
    console.log("Hello User");
}

// CALL THE FUNCTION
// INVOKE THE FUNCTION 5 times
sayHello();
sayHello();
sayHello();
sayHello();
sayHello();


// name function is usually a verb
// dynamic
// make the function accept values
// parameters

function getSum (num1, num2) {
    const a = num1;
    const b = num2;
    console.log(a+b);
}

function getSumTwo (num1, num2) {
    const sum = num1+num2;
    const multiplication = sum * 2;
}

// // arguments
getSum(20, 2);
// num1 = 20
// num2 = 2
getSum(40, 100);
// num1 = 40
// num2 = 100


//function that sayHello to a specific user
// Hello John
// Hello Tom

function sayHello (user) {
    console.log(`Hello ${user}`);
}

sayHello("John");
sayHello("Tom")
sayHello(prompt("what is your name"))


function sayHelloTwo (user, age) {
    console.log(`Hello ${user}, you are ${age} years old`);
}

sayHelloTwo("John", 20); //Hello John you are 20 years old
sayHelloTwo("Tom"); //Hello Tom, you are undefined years old

// DEFAULT PARAMETERS
function sayHelloThree (user, age="30") {
    console.log(`Hello ${user}, you are ${age} years old`);
}

sayHelloThree("John", 20); //Hello John you are 20 years old
sayHelloThree("Tom"); //Hello Tom, you are 30 years old

function sayHelloFour (user, age) {
    if(age === undefined) {
        console.log("Problem");
    } else {
        console.log(`Hello ${user}, you are ${age} years old`);
    }
}

sayHelloFour("John", 20); //Hello John you are 20 years old
sayHelloFour("Tom"); //Hello Tom, you are 30 years old