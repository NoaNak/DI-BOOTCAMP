function calculateTip() {
    let billAmount = Number(prompt("What is the amount of the bill ?"));
    // Number me permet de convertir des caracateres en chiffres
    let tip;

    if (billAmount < 50){
        tip = billAmount * 0.2;
    } else if (billAmount >= 50 && billAmount <= 200){ 
            tip = billAmount * 0.15;
    } else {
        tip = billAmount * 0.1;
    }
    console.log(billAmount);
    console.log(tip);
    console.log(billAmount + tip);
}
calculateTip();
