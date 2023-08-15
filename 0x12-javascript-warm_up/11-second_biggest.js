#!/usr/bin/node
const myArr = process.argv.slice(2);

function secondBiggest (array) {
  if (!myArr || myArr.length === 1) {
    return 0;
  } else {
    let max = Number(myArr[0]);
    let max2 = Number(myArr[0]);
    for (let i = 0; myArr[i]; i++) 
    {
      console.log(`max = ${max} before`)
      console.log(`next item = ${myArr[i + 1]}`)

      if (Number(myArr[i + 1]) > max) 
      {
        max = Number(myArr[i + 1]);
      }
      console.log(`max = ${max} after`)
      console.log(`current item = ${myArr[i]}`)
      console.log(`max2 =  ${max2} before`)

      if (Number(myArr[i]) > max2 && Number(myArr[i]) < max) 
      {
          max2 = Number(myArr[i]);
      }
      console.log(`max2 =  ${max2} after`)
      console.log('--------------')

    }
    return max2;
  }
}
const ans = secondBiggest(myArr);
console.log(ans);
