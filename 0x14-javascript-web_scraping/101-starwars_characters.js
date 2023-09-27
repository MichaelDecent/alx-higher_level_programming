#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    for (const film of data.characters) {
      request.get(film, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const filmData = JSON.parse(body);
          console.log(filmData.name);
        }
      });
    }
  }
});
