#!/usr/bin/node
// Save the contents of a webpage to a file

const myTargetURL = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

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
  const results = {};
  const data = JSON.parse(body);
  for (const task of data) {
    if (task.completed) {
      results[task.userId] = (results[task.userId] + 1) || 1;
    }
  }
  console.log(results);
});
