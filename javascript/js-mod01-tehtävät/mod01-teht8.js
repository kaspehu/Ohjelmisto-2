"use strict"

const luku1 = parseInt((prompt("Anna ensimmäinen vuosiluku: ")));
const luku2 = parseInt((prompt("Anna toinen, suurempi vuosiluku luku: ")));
let output = "<h1>";

for (let i = luku1; i <= luku2; i++) {
    if ((i % 4 === 0 && i % 100 !== 0) || (i % 400 === 0)) {
        output += `<p>${i}</p>`;
    }
}
output += "</h1>";
document.querySelector(".output").innerHTML = output;