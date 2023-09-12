#!/usr/bin/node
/**
 * module containing class square that extends from old square
 */

const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    const char = c || 'X';
    const w = this.width;
    const h = this.height;
    let i;
    let j;
    for (i = 0; i < h; i++) {
      let str = '';
      for (j = 0; j < w; j++) str += char;
      console.log(str);
    }
  }
}
module.exports = Square;
