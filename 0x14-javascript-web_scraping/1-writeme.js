#!/usr/bin/node

const fs = require('fs');

const fileContent = process.argv[3];
const filePath = process.argv[2];

fs.writeFile(filePath, fileContent, 'utf-8', (error) => {
  if (error) {
    console.error('Error:', error);
  }
});
