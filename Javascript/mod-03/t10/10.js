'use strict';

document.querySelector("form").addEventListener('submit', function(evt) {
    evt.preventDefault();
    const firstname = document.querySelector('input[name=firstname]').value;
    const lastname = document.querySelector('input[name=lastname]').value;
    document.querySelector('#target').innerHTML = `Your name is ${firstname} ${lastname}`;
});
