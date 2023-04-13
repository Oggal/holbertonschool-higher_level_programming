#!/usr/bin/node
// prints the status code of a GET request

const myTargetURL = process.argv[2];

const request = require('request');

request(myTargetURL, 'GET', function (error, response, body) {
  if (error) {
    console.log('error:', error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
