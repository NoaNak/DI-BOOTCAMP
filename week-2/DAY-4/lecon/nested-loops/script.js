const colors = ["blue", "lightgreen", "red", "yellow"];

//nested loops
for (let i = 0; i < colors.length; i += 1){ 
    console.log("------------------");
    for (let j = 0; j < colors[i].length; j += 1){
        const letter = colors[i][j] //blue
        console.log(letter);
    }
    console.log("------------------");
}

// OR with FOR IN
for (let color of colors){ 
    console.log("------------------");
    for (let j = 0; j < color.length; j += 1){
        const letter = color[j]
        console.log(letter);
    }
    console.log("------------------");
}


//while the outer loop runs once
// the inner loops runs x times, here x is the length of the word
//1st outer loop
    // --> colors[i] = colors[0]
    // --> inner loop runs colors[0].length --> 4 times
//2nd outer loop
    // --> colors[i] = colors[1]
    // --> inner loop runs colors[1].length --> 10 times
//3rd outer loop
    // --> colors[i] = colors[2]
    // --> inner loop runs colors[2].length --> 3 times
//4th outer loop
    // --> colors[i] = colors[3]
    // --> inner loop runs colors[3].length --> 6 times


//go trough each color and display each letter of each color
// B
// L
// U
// E

// "blue"[0]
// 'b'
// "blue".charAt(0)
// 'b'

//0
//1
//2
//3

// inner loop runs 4 times
//blue
//1st inner loop
// j=0
// 'blue'[0] //b

// j=1
// 'blue'[1] //l

// j=2
// 'blue'[2] //u

// j=3
// 'blue'[3] //e
