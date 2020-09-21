#!/usr/bin/node
/* Rectangle class */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Print rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  // Double values
  double () {
    this.width *= 2;
    this.height *= 2;
  }

  // Rotate values
  rotate () {
    const w = this.width;
    const h = this.height;
    this.width = h;
    this.height = w;
  }
}

module.exports = Rectangle;
