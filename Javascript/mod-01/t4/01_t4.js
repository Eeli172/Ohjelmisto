'use strict';

const random = Math.random()

const user = prompt("Tell me your name.")

if (random<0.25){
    document.querySelector('#target').innerHTML = `${user}, you're Gryffindor`
}
else if (random<0.5){
    document.querySelector('#target').innerHTML = `${user}, you're Slytherin`
}
else if (random<0.75){
    document.querySelector('#target').innerHTML = `${user}, you're Hufflepuff`
}
else {
    document.querySelector('#target').innerHTML = `${user}, you're Ravenclaw`
}