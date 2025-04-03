'use strict';

const numbers = [];
let num
let i = 0
let found = false


do {
    num = +prompt(`Give ${i+1}. number `)    
    if (numbers.includes(num)) {
        found = true
    }
    else {
        numbers.push(num)
        i++
    }

} while (!found);


numbers.sort(function(a, b){return a - b});

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i])
}
