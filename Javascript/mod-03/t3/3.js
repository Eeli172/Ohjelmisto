'use strict';
const names = ['John', 'Paul', 'Jones'];


for (let name of names) {
    const div = document.querySelector('#target');
    const html = `<li>${name}</li>`
    div.innerHTML += html
    
}