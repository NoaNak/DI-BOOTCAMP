const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
const myWatchedSeriesLenght = myWatchedSeries.length;
console.log (myWatchedSeriesLenght);

const myWatchedSeriesSentence = `I watched 3 series : ${myWatchedSeries[0]}, ${myWatchedSeries[1]}, and the ${myWatchedSeries[2]}`;
console.log (myWatchedSeriesSentence);

myWatchedSeries[2] = "friends";
console.log(myWatchedSeries);

myWatchedSeries.push("prison break");
console.log(myWatchedSeries);

myWatchedSeries.splice(0, 0, "Vampire Diaries");
console.log(myWatchedSeries);

myWatchedSeries.pop("black mirror");
console.log(myWatchedSeries);

console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries);





