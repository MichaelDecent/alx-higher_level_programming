#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let output = '';
        for (let j = 0; j < this.width; j++) {
          output += c;
        }
        console.log(output);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
