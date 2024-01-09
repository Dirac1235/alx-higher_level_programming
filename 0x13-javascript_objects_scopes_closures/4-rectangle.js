#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
  
    print (a = 'X') {
      for (let i = 0; i < this.height; i++) {
        console.log(a.repeat(this.width));
      }
    }
    rotate() {
        let x = this.height;
        this.height = this.width;
        this.width = x;
    }
    double() {
        this.width *= 2;
        this.height *= 2;
    }
  }
  
module.exports = Rectangle;
  