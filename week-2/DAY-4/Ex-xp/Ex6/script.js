  
// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

function hotelCost(){
    let priceNight = 140;
    let userAnswer =prompt(" How many night will be your stay?");
    typeof userAnswer === "Number";
    if (userAnswer>=1){
        console.log(`The price of your stay will be ${priceNight*userAnswer}$`);
        return priceNight*userAnswer
       } 
        else {
        console.log("how many night will you stay ?");
        }
}
console.log(hotelCost());

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

function planeRideCost(){
    let answer= prompt(" What's your destination");
    let pPrice = 220;
    let lPrice = 183;
    let oPrice = 300
    typeof answer === "string";

    if (answer=="london"){        
        console.log(`The price for the trip is ${lPrice}$`); 
    } else if (answer=="paris"){        
        console.log(`The price for the trip is ${pPrice}$`);
        
    } else      
        console.log(`The price for the trip is ${oPrice}$`);
        return oPrice,lPrice,pPrice 
    } 

    console.log(planeRideCost());

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental. 

function rentalCarCost(){
    let rAnswer= prompt("How many day do you want to rent the car?");
    let pCar = 40;
    let percent=5;
    typeof rAnswer === "Number";
    if (rAnswer>=1){
        console.log(`The price of your rent will be ${pCar*rAnswer}$`);
        return pCar*rAnswer
       } else if (rAnswer>10){        
        console.log(`The price of your rent will be ${pCar*rAnswer}$`);
        return (pCar*rAnswer)*0.05
    } else {
        console.log("Please let us know how many night will you stay");
        }   
}
console.log(rentalCarCost());

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

function totalVacationCost(){
  
    function hotelCost(){
        let priceNight = 140;
        let userAnswer =prompt(" How many night will be your stay?");
        typeof userAnswer === "Number";
        if (userAnswer>=1){
            console.log(`The price of your stay will be ${priceNight*userAnswer}$`);
            return priceNight*userAnswer
           } 
            else {
            console.log(" How many night will you stay");
            }
    }

    function planeRideCost(){
        let answer= prompt(" What's your destination");
        let pPrice = 220;
        let lPrice = 183;
        let oPrice = 300
        typeof answer === "string";
    
        if (answer=="london"){        
            console.log(`The price for the trip is ${lPrice}$`);
            
        } 
        else if (answer=="paris"){        
            console.log(`The price for the trip is ${pPrice}$`);
            
        } 
        else      
            console.log(`The price for the trip is ${oPrice}$`);
            return oPrice,lPrice,pPrice 
        } 
    
        function rentalCarCost(){
            let rAnswer= prompt("How many day do you want to rent the car?");
            let pCar = 40;
            let percent=5;
            typeof rAnswer === "Number";
            if (rAnswer>=1){
                console.log(`The price of your rent will be ${pCar*rAnswer}$`);
                return pCar*rAnswer
               } else if (rAnswer>10){        
                console.log(`The price of your rent will be ${pCar*rAnswer}$`);
                return (pCar*rAnswer)*0.05
            } else {
                console.log("How many night will you stay");
                }   
        }
        console.log(rentalCarCost());
}

console.log(totalVacationCost());