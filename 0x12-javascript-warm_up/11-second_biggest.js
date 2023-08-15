#!/usr/bin/node
const myArr = process.argv.slice(2);

function secondBiggest (array) {
  if (!myArr || myArr.length === 1) {
    return 0;
  } else {
    myArr.sort((a, b) => a - b);
    return (myArr[myArr.length - 2]);
  }
}

const ans = secondBiggest(myArr);
console.log(ans);
