#!/usr/bin/node
// Task 9, add two numbers

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(x, y));
