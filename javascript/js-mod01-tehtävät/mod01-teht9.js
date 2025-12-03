"use strict"

const luku = parseInt(prompt("Syötä luku: "));
let alkuluku = true;
if (luku < 2) {
    alkuluku = false;
} else {
    for (let i = 2; i <= Math.sqrt(luku); i++) {
        if (luku % i === 0) {
            alkuluku = false;
            break
        }
    }
}


if (alkuluku) {
    document.querySelector(".output").textContent =
        `Syöttämäsi luku: ${luku} on alkuluku.`;
} else {
    document.querySelector(".output").textContent =
        `Syöttämäsi luku: ${luku} ei ole alkuluku.`;
}

