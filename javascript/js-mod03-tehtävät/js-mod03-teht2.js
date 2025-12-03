
const list = ["First item", "Second Item", "Third item"]
const targetElement = document.getElementById("target");
for (const item of list) {
    const liElem = document.createElement("li");
    liElem.textContent = item;
    if (item === "Second Item") {
        liElem.classList.add("my-item");
    }
    targetElement.appendChild(liElem);
}