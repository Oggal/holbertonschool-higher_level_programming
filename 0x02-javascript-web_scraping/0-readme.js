#!/usr/bin/node
// Read a file

let fileReader = require('fs');
const myTargetFile = process.argv[2];

fileReader.readFile(myTargetFile, 'utf8', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});