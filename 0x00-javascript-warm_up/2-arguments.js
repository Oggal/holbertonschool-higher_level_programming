#!/usr/bin/node
// Task 2, arguments

const { argv } = require('node:process');

const argc = argv.length;
const values = ['No argument', 'Argument found', 'Arguments found'];
console.log(values[Math.min((argc - 2), 2)]);
