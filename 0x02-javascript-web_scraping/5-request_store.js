#!/usr/bin/node
// Save the contents of a webpage to a file

const myTargetURL = process.argv[2] || 'http://loripsum.net/api';
const fileName = process.argv[3] || 'fetched';

const request = require('request');

const requestData = {
  url: myTargetURL,
  method: 'GET'
};

function WriteToFile (file, contents) {
  const fileSystem = require('fs');
  fileSystem.writeFile(file, contents, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
}

request(requestData, 'GET', function (error, response, body) {
  if (error) {
    console.log('error:', error);
    return;
  }
  WriteToFile(fileName, body);
});
