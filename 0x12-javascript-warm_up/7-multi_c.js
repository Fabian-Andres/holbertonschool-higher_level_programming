#!/usr/bin/node
/*
|   Script that prints prints x times “C is fun”
*/
const arg1 = process.argv[2];

if (arg1 === undefined) {
    console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
