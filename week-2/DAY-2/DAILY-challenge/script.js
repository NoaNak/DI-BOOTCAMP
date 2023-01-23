let sentence = "The movie is not that bad, I like it"
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
console.log(wordNot);
console.log(wordBad);

if(wordBad > wordNot){
    console.log("The movie is good, I like it")
}

else{
    console.log("The is is good, I like it")
}