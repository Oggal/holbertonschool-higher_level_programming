#!/usr/bin/node
// Task 3, First or no arguments
let i = 1;
const values = ['No argument', process.argv[2]];
if (values[1] === undefined) {
  i--;
}
console.log(values[i]);
