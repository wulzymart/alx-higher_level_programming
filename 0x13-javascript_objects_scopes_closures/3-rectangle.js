#!/usr/bin/node
/**
 * Module containg class Rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const w = this.width;
    const h = this.height;
    let i;
    let j;
    for (i = 0; i < h; i++) {
      let str = '';
      for (j = 0; j < w; j++) str += 'X';
      console.log(str);
    }
  }
}
module.exports = Rectangle;
