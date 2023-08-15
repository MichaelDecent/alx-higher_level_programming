#!/usr/bin/node
exports.esrever = function (list) {
  const tempArr = [];
  let j = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    tempArr[j] = list[i];
    j++;
  }
  for (let i = 0; tempArr[i]; i++) {
    list[i] = tempArr[i];
  }
  return list;
};
