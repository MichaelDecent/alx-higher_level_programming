#!/usr/bin/node

const sqaureSize = process.argv[2];
if (!sqaureSize || !Number(sqaureSize)) {
  console.log('Missing size');
}

for (let i = 0; i < sqaureSize; i++) {
  let output = '';
  for (let j = 0; j < sqaureSize; j++) {
    output += 'X';
  }
  console.log(output);
}