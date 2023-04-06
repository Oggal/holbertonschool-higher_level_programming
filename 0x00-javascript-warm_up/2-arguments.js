#!/usr/bin/node
// Task 2, arguments

const { argv } = require('node:process');

let argc = argv.length;
const values = ['No argument', 'Argument found', 'Arguments found'];
argc = values[Math.min((argc - 2), 2)];

console.log(argc);
