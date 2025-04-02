'use strict';

const name = prompt('Give your name: ')
const age = +prompt('Give your age: ')

document.querySelector('#name').innerHTML =
    `Good morning ${name}!`;

if (age < 18) {
    document.querySelector('#number').innerHTML =
        "You're a minor"
}
else {
    document.querySelector('#number').innerHTML =
        "You're an adult"
}