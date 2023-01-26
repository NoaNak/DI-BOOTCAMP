  
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