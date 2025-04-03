'use strict';

const participants = +prompt("Give the number of participants:")

const names = [];

for (let i = 0; i < participants; i++) {
    names[i] = prompt(`Give ${i+1}. name:`)
}

names.sort();

for (let i = 0; i < participants; i++) {
    document.querySelector('#tehtava').innerHTML += "<li>" + names[i] + "</li>"
}