'use strict';

function roll_dice(sides) {
    return Math.floor(Math.random()*sides)+1;
};

const dice_sides = +prompt("Give the number of sides on the dice: ")
let result;

do {
    result = roll_dice(dice_sides);
    document.querySelector('#tehtava').innerHTML += "<li>" + result + "</li>";

} while (result !== dice_sides);