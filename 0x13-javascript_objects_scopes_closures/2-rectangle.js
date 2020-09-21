#!/usr/bin/node
/* Rectangle class */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 ||
        w === undefined || h === undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
