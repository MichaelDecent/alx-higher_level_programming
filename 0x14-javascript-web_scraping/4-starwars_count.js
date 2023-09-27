#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    for (const value of data.results) {
      for (const element of value.characters) {
        if (element === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
