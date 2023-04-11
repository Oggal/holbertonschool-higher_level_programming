#!/usr/bin/node
// Task 9, Log Me

let printed = 0;

exports.logMe = function (item) {
  console.log(printed + ': ' + item);
  printed++;
};
