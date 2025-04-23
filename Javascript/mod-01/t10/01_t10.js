'use strict';

let dices = +prompt("Give an amount of dices:")
let sum_wanted = +prompt("Give the sum you want to get from the dices:")
const iterations = 10000
let times = 0
let sum

for (let i = 0; i < iterations; i++) {
    sum = 0
    for (let j = 0; j < dices; j++) {
        sum += (Math.floor(Math.random()*6)+1)
    }
    if (sum === sum_wanted) {
        times++
    }
};

document.querySelector('#dice').innerHTML = `Probability to get sum ${sum_wanted} with ${dices} dice is ${(times/iterations*100).toFixed(2)}%`