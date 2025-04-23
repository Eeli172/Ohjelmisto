'use strict';

function even(array) {
    const array_even = [];
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            array_even.push(array[i]);
        };
    };
    return array_even;
};

const array_all = [2, 7, 4, 6, 9, 1, 8, 16, -6, -5, -4, -3];
const array_even = even(array_all);

console.log(`The original array: ${array_all}`)
console.log(`The modified array: ${array_even}`)