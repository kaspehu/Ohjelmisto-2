"use strict"

const form = document.querySelector("#searchForm");
const input = document.querySelector("#query");
const resultsDiv = document.querySelector("#results");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const searchValue = input.value.trim();
    if (searchValue.length < 3)
        return;

    resultsDiv.innerHTML = "";

    const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(searchValue)}`;
    const response = await fetch(url);
    const results = await response.json();

    for (const result of results) {
        const show = result.show;

        const article = document.createElement("article");

        const title = document.createElement("h2");
        title.textContent = show.name;
        article.appendChild(title);

        const link = document.createElement("a");
        link.href = show.url || "Url not found."
        link.target = "_blank";
        article.appendChild(link);

        const img = document.createElement("img");
        img.src = show.image?.medium || "https://placehold.co/210x295?text=Not%20Found";
        img.alt = show.name;
        article.appendChild(img);

        const summaryDiv = document.createElement("div");
        summaryDiv.innerHTML = show.summary || "Summary not found";
        article.appendChild(summaryDiv);

        resultsDiv.appendChild(article);


    }
});
