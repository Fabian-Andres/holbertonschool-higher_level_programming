#!/usr/bin/node
/* Rectangle class */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 ||
          w === undefined || h === undefined) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // Print rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let str = 'X';
      for (let j = 1; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
