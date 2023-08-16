#!/usr/bin/node
let count = 0;
exports.logMe = function counting (item) {
  count++;
  console.log(`${count}: ${item}`);
};
