#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    for (const value of data.results) {
      for (const element of value.characters) {
        if (element.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
