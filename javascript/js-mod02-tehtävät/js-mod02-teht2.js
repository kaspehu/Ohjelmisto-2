
const lista = [];
const listapituus = parseInt(prompt("Syötä henkilölukumäärä:"));


for (let i = 0; i < listapituus; i++) {
    const henkilo = (prompt("Anna henkilön nimi: "));
    lista.push(henkilo);
}

lista.sort()

const listaOlElement = document.createElement("Ol");
for (const i of lista) {
    const liElem = document.createElement("li");
    liElem.textContent = i;
    listaOlElement.appendChild(liElem);
}
document.body.appendChild(listaOlElement);
