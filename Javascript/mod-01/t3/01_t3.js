'use strict';

const first = +prompt("Give 1. integer");
const second = +prompt("Give 2. integer");
const third = +prompt("Give 3. integer");

const sum =  first + second + third
const product = first * second * third
const avg = (first + second + third) / 3

document.querySelector('#sum').innerHTML = `Sum of given numbers: ${sum}`;
document.querySelector('#product').innerHTML = `Product of given numbers: ${product}`;
document.querySelector('#avg').innerHTML = `Average of given numbers: ${avg}`;


