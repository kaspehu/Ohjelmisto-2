'use strict';
const names = ['John', 'Paul', 'Jones'];
for (const name of names) {
    document.getElementById('target').innerHTML += `<li>${name}</li>`;
}