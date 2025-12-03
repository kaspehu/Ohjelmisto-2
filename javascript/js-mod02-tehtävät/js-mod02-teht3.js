
const lista = [];
const listapituus = 6


for (let i = 0; i < listapituus; i++) {
    const koira = (prompt("Anna koiran nimi: "));
    lista.push(koira);
}

lista.sort()
lista.reverse()

const listaUlElement = document.createElement("Ul");
for (const i of lista) {
    const liElem = document.createElement("li");
    liElem.textContent = i;
    listaUlElement.appendChild(liElem);
}
document.body.appendChild(listaUlElement);
