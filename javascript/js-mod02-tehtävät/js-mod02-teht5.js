
const numerolista = [];
let numero = parseInt(prompt("Syötä luku: "));

while (!numerolista.includes(numero)) {
    numerolista.push(numero)
    numero = parseInt(prompt("Syötä luku (jokin aiemmin syötetty luku lopettaa): "))
}

numerolista.sort();
console.log(numerolista);