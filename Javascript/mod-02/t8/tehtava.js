'use strict';

function concat(array) {
    let string = "";
    for (let i = 0; i < array.length; i++) {
        string += array[i];
    };
    return string;
};

const array = ["Johnny", "DeeDee", "Joey", "Marky"];
let string = concat(array);

document.querySelector('#tehtava').innerHTML = string;
