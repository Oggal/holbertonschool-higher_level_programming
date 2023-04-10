#!/usr/bin/node
// Task 11, second largest

const x = process.argv[3];

if (typeof x !== 'undefined') {
  console.log(0);
}

let max = 0;
let betamax = max;

for (const cur of process.argv.length) {
  if (max < cur) {
    betamax = max;
    max = cur;
  }
}
console.log(betamax);
