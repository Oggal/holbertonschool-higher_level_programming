#!/usr/bin/node
// write to a file

const fileReader = require('fs');
const myTargetFile = process.argv[2];
const myContent = process.argv[3];

fileReader.writeFile(myTargetFile, myContent, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
