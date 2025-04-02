'use strict';

const num = +prompt("Give an integer to check if it is prime number or not:")

let prime = true 
for (let i = 2; i < num && prime; i++) {
    console.log(i)
    if (num !== i && num % i === 0) { 
        prime = false
    }
}

if (prime) {
    document.querySelector('#prime').innerHTML = `${num} is a prime number. `;
}
else {
    document.querySelector('#prime').innerHTML = `${num} is not a prime number. `;
}