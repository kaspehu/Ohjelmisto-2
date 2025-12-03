
const numerolista = [];

for (let i = 0; i < 5; i++) {
    let luku = parseInt(prompt("Anna luku: "));
    numerolista.push(luku);
}
for (let i = 0; i < numerolista.length; i++) {
    console.log(numerolista[4-i]);
}