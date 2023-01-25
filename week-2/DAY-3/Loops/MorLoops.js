const users = [
    {
        username:"John",
        lastName: "Smith"
    },
    {
        username:"Tom",
        lastName: "Smith"
    },
    {
        username:"Lea",
        lastName: "Smith"
    }
];

// // users[0]["username"]
// // users[1]["username"]
// // users[2]["username"]

// // console.log(users);

// //go over the array, and for each person displuay the fullname
for(let i = 0; i <= users.length-1; i++){
    const fullName = users[i]["username"] + " " + users[i]["lastName"];
    console.log(fullName);
}

const colors = ["blue", "red", "yellow"]
// colors[0] = "green"

// //array
for (let color of colors){
    console.log(`The color is ${color}`);
}

// console.log(colors);
// The color is blue
// The color is red
// The color is yellow

// 1st loop
// color = "blue"

// 2nd loop
// color="red"


const user = {
    username:"John",
    lastName: "Smith",
}

// //for in //OBJECTS
for (let key in user){
    console.log(key);
    console.log(user[key]);
}



//break out
//continue

// //if the fruit has more or equal than 5 letters, then you log it
// //else you break out of the loop - stop the loop
const fruits = ["apple", "banana", "pear", "melon"];

for (let i = 0; i< fruits.length; i++){
    if(fruits[i].length <= 5){
        console.log(fruits[i]);
    } else {
        console.log("not correct");
        break;
    }
}

// // 1 loop
// // apple.lenght <= 5 --> true --> log

// // 2 loop
// // banana.lenght <= 5 --> false --> break;

//continue skip the elememt
for (let i = 0; i< fruits.length; i++){
    if(fruits[i].length <= 5){
        console.log(fruits[i]);
    } else {
        console.log("not correct");
        continue;
    }
}

// for loop : starting point and ending point

//GUESSING GAME : WHILE
//Ask the user to give you the name of a city
//if the city is not Paris you ask again

let userAnswer = prompt("what is the city I'm thikimg about").toLowerCase();

while (userAnswer !== "paris") {
    console.log(`You answered ${userAnswer}`);
    userAnswer = prompt("what is the city I'm thikimg about").toLowerCase();
}

console.log("CORRECT THE CITY IS PARIS");

// while(condition) {
//     //statement
// }


let raining = true;
let num = 10

while(raining){
    console.log("don't go out");
    if (num === 10) {
        break
    }
}