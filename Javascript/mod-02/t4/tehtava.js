'use strict';

const numbers = [];
let num
let i = 0

do {
    num = +prompt(`Give ${i+1}. number `)    
    numbers.push(num)
    i++
} while (num !== 0);


numbers.sort(function(a, b){return a - b});

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i])
}
