'use strict';

let output;
if (confirm("Should I calculate the square root?")) {
    const num = +prompt("Give a number: ")
    if (num >= 0) {
      output = `Square root of ${num} is ${Math.sqrt(num)}`;
    }  
    else {
      output  ="The square root of a negative number is not defined"
    }
}   
else {
  output = "The square root is not calculated.";
}

document.querySelector('#sqrt').innerHTML = output;