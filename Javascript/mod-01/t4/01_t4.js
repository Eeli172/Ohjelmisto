'use strict';

const student_name = prompt("Give your name: ")

let result;
result = Math.floor(Math.random()*4)+1;

switch (result) {
    case 1:
        document.querySelector('#sorting_hat').innerHTML = `${student_name}, you are Gryffindor.`;
        break;
    case 2:
        document.querySelector('#sorting_hat').innerHTML = `${student_name}, you are Slytherin.`;
        break;
    case 3:
        document.querySelector('#sorting_hat').innerHTML = `${student_name}, you are Hufflepuff.`;
        break;
    case 4:
        document.querySelector('#sorting_hat').innerHTML = `${student_name}, you are Ravenclaw.`;
        break;
}