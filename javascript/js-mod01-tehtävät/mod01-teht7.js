"use strict"

const heittomäärä = parseInt(prompt("Montako nopanheittoa?: "));
let summa = 0;
for (let i = 0; i < heittomäärä; i++) {
    const noppa = Math.ceil(Math.random() * 6);
    console.log(noppa);
    summa += noppa;
}

const result = `Heittämiesi noppien summa: ${summa}`;
document.querySelector(".output").textContent = result;
