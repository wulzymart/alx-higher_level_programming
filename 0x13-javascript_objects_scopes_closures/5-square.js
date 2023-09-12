#!/usr/bin/node
/**
 * module containing class square that extends from rectangle
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
