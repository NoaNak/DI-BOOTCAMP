let myNumber = 23;
// la variablel sapl mynumber et est egale a 23
// la valeur de la variable est 23
// 23 est un nombre

console.log(myNumber); 

let pet = "cats";
console.log(pet); 
// ceci me donne la valeur de la variable pet donc = cats
console.log("pet");
// ceci est un string avec la valeur de pets

pet = "dog";
// console.log(pet); // dog

const johnAge = 23;
const johnName = "john";
const johnPet = "rabbit";

console.log(johnAge);
// johnAge = 54; 
// erreur, on ne peut pas changer la variable avec un const

let computer = "Mac";
//  je declare la variable, la valeur est mac

let day = 
day = "sunday";
// je declare la variable day
// je definie la variable "sunday"

let friend = "john";
friend = "tom"; 
// je peut redefinir la variable avecn let
let time = 12;

// CONCATENATION
const sentence = "john and tom are working on Sunday at 12 pm";
const sentenceOne = "john and" + friend + "are working on" + day + "at" + time + pm;
console.log(sentenceOne);

// TEMPLATE LITERALS BACTICK : RECOMMENDER 
const sentenceTwo = `john and ${friend} are working on ${day}`;
console.log(sentenceTwo);
// cest deux sentence sont les meme mais ecrites dfferements 


JAVASCRIPT
DATA TYPES - PRIMITIVE DATA TYPES
- String
- Number
- Boolean 
- undefined - the variable is not defined
- null - the variable is defined but the value is null -
// ex:
// let happy;
// --> undefined

// let house = null;
// --> value is null

COMPARAISON
- == : compare the value
and the result will be a Boolean
- == : compare the value and the data type 
and the result will be a Boolean
- ! : means not 
- !true: means false


variable
- DECLARE VARIABLE with the keybord let or const
- NAME VARIABLE camel case myPhoneIsBlue
- DEFINE VARIABLE
// declare and define at the same time
// let pet 



const password = "hello1234";
// property length
const lengthPassword = password.length; 

// "Paris" == "paris"
// false
// "Paris".toLowerCase()
// 'paris'


// METHOD NEED ()
const answer = prompt('where do you want to travel ?');
// whatever the prompt returns will be saved into the variable
// PARIS or PAriS
// to make sure that the comparaison is true, I need to convert the string to lowercase
console.log(answer.toLowerCase ()=="paris");

// TO CHAIN METHODS
const mood = "happy";
console.log(mood.toUpperCase().length);


