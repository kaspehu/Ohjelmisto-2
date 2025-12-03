"use strict";

console.log("I'm printing to console!")

const name = prompt("Anna nimesi: ")
const greeting = `Hei, ${name}!`;
document.querySelector(".output").textContent = greeting;

const luku1 = parseInt(prompt("Anna luku: "));
const luku2 = parseInt(prompt("Anna luku: "));
const luku3 = parseInt(prompt("Anna luku: "));

const summa = luku1 + luku2 + luku3;
const tulo = luku1 * luku2 * luku3;
const keskiarvo = (luku1 + luku2 + luku3) / 3;
const summaprint = `Lukujen summa: ${summa}`;
const keskiarvoprint = `Lukujen keskiarvo: ${keskiarvo}`;
const tuloprint = `Lukujen tulo: ${tulo}`;
document.querySelector(".output2").textContent = summaprint;
document.querySelector(".output3").textContent = keskiarvoprint;
document.querySelector(".output4").textContent = tuloprint;
const gryffindor = `The hat has chosen your fate, ${name}, your house is Gryffindor`
const slytherin = `The hat has chosen your fate, ${name}, your house is  Slytherin`
const hufflepuff = `The hat has chosen your fate, ${name}, your house is  Hufflepuff`
const ravenclaw = `The hat has chosen your fate, ${name}, your house is  Ravenclaw`


const result = Math.ceil(Math.random()*4);
switch(result) {
    case 1:
        document.querySelector(".output5").textContent = gryffindor;
        break;
    case 2:
        document.querySelector(".output5").textContent = slytherin;
        break;
    case 3:
        document.querySelector(".output5").textContent = hufflepuff;
        break;
    case 4:
        document.querySelector(".output5").textContent = ravenclaw;
        }
