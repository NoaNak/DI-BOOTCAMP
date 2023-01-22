// complex data type 

// let shopping = ["chocolate", "shoes", "apple"];

// let all = [12, "hello", true, ["apple", "melon"]];

const colors = ["blue", "red", "yellow"];
const favoriteColor = [1];
// on commence a compter a partir de 0 donc le red a la position de 1 (nameArray) c la position de lelement
const sentence = `My favorite colors is ${favoriteColor}`;
console.log(sentence);

const hatedColor = color[3][0]; // ["white", "black"]
console.log(hatedColor); // white

// change yellow to orange
// i need to find the position of yellow
colors[2] = "orange";
console.log(colors);

const positionWhite = colors.indexOf("white");
console.log(positionWhite); // not found: -1

const fruit = ["apple", "banana", "pear"];
const lastItem = fruit[2]

position last item : 2
length : 3

const lengthArray = fruits.lenght // 3
const positionOfLastElement = lengthArray-1;
const lastElement = fruits[positionOfLastElement]; //fruits[3-1] //fruits[2]

// add an element at the end of the array
fruits.push("melon");
// ["apple", "banana", "pear", "melon"];

// delete an element from the end of the array
fruits.pop();
// ["apple", "banana", "pear"];

//delete or add elements within the array

// splice(start index, how many elements I want to delete, what elements I want to add)


const myFruits = ["apple", "banana", "pear"];
// add between apple and banana
myFruits.splice(1, 0, "melon");
console.log(myFruits);

// ['apple', 'melon', 'banana', 'pear']
// delete banana and pear
myFruits.splice(2, 2)
// I want to start deleting at position 2
// and I want to delete 2 elements
// ['apple', 'melon']


console.log(myFruits);