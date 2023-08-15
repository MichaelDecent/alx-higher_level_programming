#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  }
  return factorial(num - 1) * (num);
}
const result = factorial(process.argv[2]);
console.log(result);
