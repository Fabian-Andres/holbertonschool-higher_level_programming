#!/usr/bin/node
/*
|   Script that prints a square
*/
let arg1 = process.argv[2];
arg1 = parseInt(arg1, 10);

if (Number.isNaN(arg1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg1; i++) {
    let str = 'X';
    for (let j = 0; j < arg1; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
