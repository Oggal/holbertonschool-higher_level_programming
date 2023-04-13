#!/usr/bin/node
// prints the movie title

const myTargetURL = process.argv[2];

const request = require('request');

const requestData = {
  url: myTargetURL,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

request(requestData, 'GET', function (error, response, body) {
  if (error) {
    console.log('error:', error);
    return;
  }
  const films = JSON.parse(body).results;
  let charCount = 0;
  for (const film of films) {
    for (const char of film.characters) {
      if (char.includes('18')) {
        charCount++;
      }
    }
  }
  console.log(charCount);
});
