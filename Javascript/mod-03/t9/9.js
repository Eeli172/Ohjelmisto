'use strict';

document.querySelector("#start").addEventListener('click', function() {
    const calculation = document.querySelector('input[id=calculation]').value;
    const p = document.querySelector('#result');

    if (calculation.includes("+")) {
        const numbers = calculation.split('+')
        p.innerHTML = `The result is: ${+numbers[0] + +numbers[1]}`
    }
    else if (calculation.includes("-")) {
        const numbers = calculation.split('-')
        p.innerHTML = `The result is: ${+numbers[0] - +numbers[1]}`
    }
    else if (calculation.includes("*")) {
        const numbers = calculation.split('*')
        p.innerHTML = `The result is: ${+numbers[0] * +numbers[1]}`
    }
    else if (calculation.includes("/")) {
        const numbers = calculation.split('/')
        p.innerHTML = `The result is: ${+numbers[0] / +numbers[1]}`
    }

})