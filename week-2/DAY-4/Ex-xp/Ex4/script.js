const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"]

function myBill(){
    let total = 0;
    for (let i = 0; i < shoppingList.length; i++){
        let item = shoppingList[i];
        if (item in stock){
            if (stock[item] > 0){
            total += prices[item];
            } else {
             console.log(`${item} is not in stock`);
            } 
        } else {
             console.log(`i don't sell ${item}`);
        }
    }
}
console.log(myBill());

// do a verification wth lyse/shaun
