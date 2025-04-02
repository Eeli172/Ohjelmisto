'use strict';

const start_year = prompt("Start year:")
const end_year = prompt("End year:")

for (let i=start_year; i <= end_year; i++) { // for loop to iterate the given years
    if (i % 4 === 0) { // if current year is divisible by 4
        if (i % 100 === 0 && i % 400 !== 0) { // if current year is divisible by 100 and not by 400 (to exclude those from leap years)
        }
        else { // leap years
            const li_element = document.createElement("li"); // create a new <li> element
            li_element.appendChild(document.createTextNode(i)); // add the leap year to the <li> element
            const ul_element = document.getElementById("leap"); // get the <ul> element by id
            ul_element.appendChild(li_element); // add the <li> element to the <ul> element
        }
    }
}
