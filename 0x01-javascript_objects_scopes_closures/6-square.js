#!/usr/bin/node
const myBase = require('./5-square');

module.exports = class Square extends myBase {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
