#!/usr/bin/node
// Task 11, second largest

if (process.argv.length <= 3) {
  console.log(0);
}

const arr = process.argv.slice(2);
let max = arr[0];
let second = arr[0];

for (let i = 0; i < arr.length; i++) {
  const curr = parseInt(arr[i]);
  if (curr > max) {
    second = max;
    max = curr;
  }
}

console.log(second);
