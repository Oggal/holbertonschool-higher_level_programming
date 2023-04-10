#!/usr/bin/node
// Task 5, To Integer

const inValue = process.argv[2];
if (isNaN(inValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(inValue));
}
