#!/usr/bin/node
// Task 2, arguments

const { argv } = require('node:process');

const argc = argv.length;
const values = ['No argument', 'Argument found', 'Arguments found'];
if (argc === 3) {
  console.log(values[argc - 2]);
} else {
  console.log(values[argc - 2]);
}
