#!/usr/bin/node
const myArr = process.argv.slice(2);

function secondBiggest (array) {
  if (!myArr || myArr.length === 1) {
    return 0;
  } else {
    let max = 0;
    let max2 = 0;
    for (let i = 0; myArr[i + 1]; i++) {
      if (myArr[i + 1] > myArr[i]) {
        max = myArr[i + 1];
        max2 = myArr[i];
        if (myArr[i + 1] > max2 && myArr[i + 1] !== max) {
          max2 = myArr[i + 1];
        }
      }
    }
    return max2;
  }
}
const ans = secondBiggest(myArr);
console.log(ans);
