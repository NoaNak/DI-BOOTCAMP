// console.log("hello");
// console.log("hello");
// console.log("hello");
// console.log("hello");
// console.log("hello");

//repeat an action a certain number of time : loops
// SYNTAX
// for (starting point;condition;increment/decrement) {
//     //statement
// }

for (let counter = 1; counter <=3; counter += 1) {
    console.log(`The counter is equal to ${counter}`);
}

// 1st loop
// counter = 1
// counter <=3 --> true
// The counter is equal to 1
// counter = 2


// // 2nd loop
// counter = 2
// counter <=3 --> true
// enter the loop
// The counter is equal to 2
// counter = 3

// // 3rd loop
// counter = 3
// counter <=3 --> true
// enter the loop
// The counter is equal to 3
// counter = 4

// // 4th loop
// counter = 4
// counter <=3 --> false
// we go out, we don't enter the loop again

//the same
for (let counter = 1; counter <=3; counter += 1) {
    console.log(`Hello`);
}

//the same
for (let counter = 22; counter <=25; counter += 1) {
    console.log(`Hello`);
}

// GAME

let numberOfPoints = 10;

// the user starts with 10 points
// we want to add him a point (one at a time) until 5 points
// how many times the loop run - 5 TIMES
for (let counter = 1; counter <= 5; counter ++){
    numberOfPoints += 1;
    console.log(numberOfPoints);
}

// 10 
// 11
// 12
// 13
// 14
// 15


let num = 10;
num = num + 1;
// SHORTCUT
num += 1;
//SHORTCUT
num ++

// GAME

// const fruits = ["apple", "banana", "pear", "melon"];
//goal : modify the array so that every element is in plural
// ["apples", "bananas", "pears", "melons"]

// console.log(fruits[0]);
// console.log(fruits[1]);
// console.log(fruits[2]);
// console.log(fruits[3]);

// fruits[x]
// x = 0
// x = 1
// x = 2
// x = 3

for (let x = 0; x <= 3; x++){
    console.log(fruits[x]);
}




// 1st loop
// x = 0
// x <= 3 --> true
// fruits[0] --> apple
// x = 1

// // 2nd loop
// x = 1
// x <= 3 --> true
// fruits[1] --> banana

// fruits[0] = fruits[0] + "s"
// fruits[0] += "s" 
// fruits[1] += "s"
// fruits[2] += "s"
// fruits[3] += "s"


for (let x = 0; x < fruits.length; x++){
    fruits[x] += "s";
}

//if the fruit doens't contain the word "melon" we add an 's'
for (let x = 0; x <= fruits.length-1; x++){
    if (!fruits[x].includes("melon")) {
        fruits[x] += "s";
    } else {
        fruits[x] += "~";
    }
}

console.log(fruits);