// Ex1

const userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};


//add
userCart["lastname"] = "Smith";

//modify
userCart["username"] = "Tom";

// change the price of the pear 
// je multiplie le tout 
userCart["prices"]["pear"] *= 1.17;
console.log(userCart);

const userChoise = prompt('what fruit do you want ?').toLocaleLowerCase();
console.log(userChoise);
// tolower... selectionne tout type decriture

// console.log the price for the specific fruit do you want to use 
const value = userCart["prices"][userChoise];
console.log(`The price of ${userChoise} is ${value} dollars`);


// Ex2

const family = {
    lastName : "Smith",
    members : 3,
    names : ["John", "Tom", "Diana"],
    isInVacation: true,
}

family["isInvacation"] = false;
console.log(family);

