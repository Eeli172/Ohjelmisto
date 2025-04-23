'use strict';

const div = document.querySelector('#target');

const t1 = document.createTextNode('First item');
const t2 = document.createTextNode('Second item');
const t3 = document.createTextNode('Third item');

const p1 = document.createElement('li');
const p2 = document.createElement('li');
const p3 = document.createElement('li');

p1.appendChild(t1);
p2.appendChild(t2);
p3.appendChild(t3);

div.appendChild(p1);
div.appendChild(p2);
div.appendChild(p3);