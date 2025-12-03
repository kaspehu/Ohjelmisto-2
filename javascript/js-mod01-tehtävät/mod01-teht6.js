"use strict"

const kysymys = confirm("Do you want to calculate square root?");
    if (kysymys === true) {
        const luku1 = parseInt(prompt("Insert a number: "));
            if (luku1 > 0) {
                const sqrt = Math.sqrt(luku1);
                const vastaus = `The square root of you number is: ${sqrt}.`;
                document.querySelector(".output").textContent = vastaus;
            } else {
                const vastaus2 = "The square root of a negative number is not defined";
                document.querySelector(".output").textContent = vastaus2;
            }
        }
    else {
        const vastaus3 = "The square root is not calculated.";
        document.querySelector(".output").textContent = vastaus3;
}




