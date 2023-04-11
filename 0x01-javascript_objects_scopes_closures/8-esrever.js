#!/usr/bin/node
// Task 8, Reverse

exports.esrever = function (list) {
  const results = [];
  for (let i = list.length - 1; i >= 0; i++) {
    results.append(list[i]);
  }
  return results;
};
