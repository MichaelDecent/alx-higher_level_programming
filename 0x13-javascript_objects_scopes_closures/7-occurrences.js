#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  if (list) {
    for (let i = 0; list[i]; i++) {
      if (list[i] === searchElement) {
        total++;
      }
    }
  }
  return total;
};
