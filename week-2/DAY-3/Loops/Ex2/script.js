
// Create a variable sum equals to 0
// Loop over this array, to get the sum of all the numbers
// Where should you console log the sum ?
// let prices = [23, 15, 34, 10];
// let sum = 0;

 let prices = [23, 15, 34, 10];
 let sum = 0;
// i means index
for(let i = 0; i < prices.length; i++) {
  sum += prices[i];
}
console.log("The sum of all numbers is: " + sum);
