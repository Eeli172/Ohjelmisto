'use strict';

const dice_amount = +prompt("Give the amount of dices to throw: ")
const result_wanted = +prompt("Give the sum of the eye numbers you want from the dice(s): ")
const loop_times = 10000
let correct = 0
let result_total

for (let i = 0; i < loop_times; i++) {
    result_total = 0
    for (let j = 0; j < dice_amount; j++) {
        result_total += Math.floor(Math.random() * 6) + 1
    }
    if (result_total === result_wanted) {
        correct++
    }
}

let probability = (correct / loop_times * 100).toFixed(2)
document.querySelector('#dice').innerHTML = `Probability to get sum ${result_wanted} with ${dice_amount} dice is ${probability}%`
