'use strict';

document.querySelector("#start").addEventListener('click', function() {
    const num1 = +document.querySelector('input[id=num1]').value;
    const num2 = +document.querySelector('input[id=num2]').value;
    const p = document.querySelector('#result');
    const operation = document.querySelector('#operation').value;

    switch (operation) {
        case 'add':
            p.innerHTML = `The result is: ${num1 + num2}`
            break;

        case 'sub':
            p.innerHTML = `The result is: ${num1 - num2}`
            break;

        case 'multi':
            p.innerHTML = `The result is: ${num1 * num2}`
            break;

        case 'div':
            p.innerHTML = `The result is: ${num1 / num2}`
            break;

    }
})
