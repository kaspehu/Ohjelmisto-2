"use strict"

async function searchTVMaze(searchString) {
    const response = await fetch("https://api.tvmaze.com/search/shows?q=" + searchString);
    const results = await response.json();
    console.log("tv maze results", results);
    return results;
}

const searchForm = document.querySelector("form#tvmaze");
const inputText = searchForm.querySelector("input");
searchForm.addEventListener("submit", async function(event) {
    event.preventDefault();
    if (inputText.value.length > 1) {
        const tvMazeResults = await searchTVMaze(inputText.value);
        console.log("Event handler results", tvMazeResults);
    }
});