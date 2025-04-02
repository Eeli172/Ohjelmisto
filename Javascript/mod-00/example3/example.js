'use strict';

const name = prompt('Anna nimesi: ')
const num = +prompt('Anna numerosi: ')


document.querySelector('#name').innerHTML =
    `Good morning ${name}!`;
document.querySelector('#number').innerHTML =
    `You are ${num} years old`