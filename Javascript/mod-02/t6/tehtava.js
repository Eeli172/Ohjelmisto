'use strict';

function roll_dice() {
    return Math.floor(Math.random()*6)+1;
};


let result;

do {
    result = roll_dice();
    document.querySelector('#tehtava').innerHTML += "<li>" + result + "</li>";

} while (result !== 6);