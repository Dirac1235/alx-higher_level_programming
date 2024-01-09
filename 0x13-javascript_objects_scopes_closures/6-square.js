#!/usr/bin/node
const Squarep = require('./5-square.js');
class Square extends Squarep {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
}
module.exports = Square;
