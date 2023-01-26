function changeEnough(itemPrice,amountOfChange) {
    const ourArray = [25, 20, 5, 0];
    let sum = 0;
    for (let i = 0; i < ourArray.length; i += 1) {
      sum += ourArray[i];
    }
   console.log(sum);
    if(itemPrice>=sum){
        console.log("true")
    } else{
        console.log("false")
    }
  }
  console.log(changeEnough(4.35,[25, 20, 5, 0]));