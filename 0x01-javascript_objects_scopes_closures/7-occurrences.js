#!/usr/bin/node
// Task 7, Occurances

exports.nbOccurences = function (list, searchElement) {
  const matching = list.filter(value => value === searchElement);
  return matching.length;
};
