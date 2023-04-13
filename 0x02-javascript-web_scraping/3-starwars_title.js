#!/usr/bin/node
// prints the movie title

const myTargetURL = 'https://swapi-api.hbtn.io/api/films/';
const movieID = process.argv[2];

const request = require('request');

const requestData = {
  url: myTargetURL + movieID,
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
  console.log(JSON.parse(body).title);
});
