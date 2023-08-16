#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach(element => {
  if (newDict[dict[element]] === undefined) {
    newDict[dict[element]] = [element];
  } else {
    newDict[dict[element]].push(element);
  }
});
console.log(newDict);
