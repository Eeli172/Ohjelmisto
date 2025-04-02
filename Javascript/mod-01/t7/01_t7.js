'use strict';

const amount = +prompt("Give a number of dice rolls:")
let dice_sum = 0

for(let i=0; i < amount; i++) {
    dice_sum += Math.floor(Math.random()*6)+1;
}

document.querySelector('#dice_sum').innerHTML = `Sum of ${amount} dices thrown: ${dice_sum}`;