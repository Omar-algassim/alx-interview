#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const endPOint = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function getData (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response) => {
      if (error) {
        console.error(error);
        reject(error);
      } else {
        resolve(JSON.parse(response.body));
      }
    });
  });
}

getData(endPOint)
  .then(data => {
    const characters = data.characters;
    const characterPromises = [];
    for (let i = 0; i < characters.length; i++) {
      characterPromises.push(getData(characters[i]));
    }
    Promise.all(characterPromises)
      .then(characterDataArray => {
        characterDataArray.forEach(characterData => {
          console.log(characterData.name);
        });
      })
      .catch(error => {
        console.error(`Error fetching character data: ${error.message}`);
      });
  })
  .catch(error => {
    console.error(`Error fetching film data: ${error.message}`);
  });
