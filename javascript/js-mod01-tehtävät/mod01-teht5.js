"use strict"

const luku1 = parseInt(prompt("Anna luku: "));
const tulos = `Antamasi vuosi ${luku1} on karkausvuosi.`;
const tulos2 =`Antamasi vuosi ${luku1} ei ole karkausvuosi.`;

if ((luku1 % 4 === 0 && luku1 % 100 !== 0) || (luku1 % 400 === 0)) {
    document.querySelector(".output").textContent = tulos;}
else {
    document.querySelector(".output").textContent = tulos2;
}
