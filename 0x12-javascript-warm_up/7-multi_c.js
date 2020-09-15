#!/usr/bin/node
/*
|   Script that prints prints x times “C is fun”
*/
let arg1 = process.argv[2];
arg1 = parseInt(arg1, 10);

if (Number.isNaN(arg1)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
