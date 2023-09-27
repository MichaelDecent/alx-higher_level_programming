#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const taskData = {};
    const data = JSON.parse(body);
    for (const val of data) {
      if (val.completed === true) {
        if (taskData[val.userId] === undefined) {
          taskData[val.userId] = 1;
        } else {
          taskData[val.userId]++;
        }
      }
    }
    console.log(taskData);
  }
});
