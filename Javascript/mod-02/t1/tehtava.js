'use strict';

const numbers = [];

for (let i = 0; i <= 4; i++) {
    numbers.push(+prompt(`Give ${i+1}. number:`))
}

for (let i = 4; i >= 0; i--) {
    console.log(numbers[i])
}