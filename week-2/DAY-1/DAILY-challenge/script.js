// EX 1

const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift("Banana");
fruits.sort();
fruits.push("Kiwi");
fruits.splice(0, 1);
fruits.reverse();
console.log(fruits);

// EX 2

const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);



