#!/usr/bin/node
/* Square class */
const Squareparent = require('./5-square');

class Square extends Squareparent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = '';
    if (c) {
      char = c;
    } else {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += char;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
