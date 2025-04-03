'use strict';

const dog_amount = 6
const names = [];

for (let i = 0; i < dog_amount; i++) {
    names.push(prompt(`Give ${i+1}. name:`))
}

names.sort();
names.reverse();

for (let i = 0; i < dog_amount; i++) {
    document.querySelector('#tehtava').innerHTML += "<li>" + names[i] + "</li>"
}