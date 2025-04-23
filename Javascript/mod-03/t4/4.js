'use strict';

const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const div = document.querySelector('#target');

for (let student of students) {
  const t = document.createTextNode(student.name);
  const p = document.createElement('option');
  p.appendChild(t);
  p.setAttribute('value', student.id); 
  div.appendChild(p);
};