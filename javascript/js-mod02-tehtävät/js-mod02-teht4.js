
const numerolista = [];
let numero = parseInt(prompt("Syötä luku: "));

while (numero !== 0) {
    numerolista.push(numero)
    numero = parseInt(prompt("Syötä luku (0 lopettaa): "))
}

numerolista.sort();
numerolista.reverse();
console.log(numerolista);