'use strict';
const first = prompt("1st num:")
const second = prompt("2nd num:")
const third = prompt("3rd num:")

document.querySelector('#sum').innerHTML = `Sum: ${first + second + third}, Product: ${first * second * third}, Average: ${(first + second + third) / 3}`
