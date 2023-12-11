#!/usr/local/bin/node
const SuperSquare = require("./5-square");

class Square extends SuperSquare {
  constructor(size) {
    super(size);
  }

  charPrint(char) {
    if (char) {
      for (let y = 0; y < this.height; y++) {
        for (let x = 0; x < this.width; x++) {
          process.stdout.write(char);
        }
        console.log("");
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
