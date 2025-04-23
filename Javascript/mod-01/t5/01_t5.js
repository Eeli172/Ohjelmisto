'use strict';

const year = +prompt("Enter a year:")
let bool = false


if (year % 4 === 0) {
    if (year % 100 === 0) {
        if (year % 400 === 0) {
            bool = true
        }
    }
    else {
        bool = true
    }
}

switch (bool) {
    case true:
        document.querySelector('#leap').innerHTML = `${year} is a leap year`
        break;
    case false:
        document.querySelector('#leap').innerHTML = `${year} is not a leap year`
        break;
}