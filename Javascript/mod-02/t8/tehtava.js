'use strict';

function concat(array) {
    let string = "";
    for (let i of array) {
        string += i;
    };
    return string;
};

const array = ["Johnny", "DeeDee", "Joey", "Marky"];
let string = concat(array);

document.querySelector('#tehtava').innerHTML = string;