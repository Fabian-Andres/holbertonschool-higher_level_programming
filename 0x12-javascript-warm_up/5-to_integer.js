#!/usr/bin/node
/*
|   Script that prints My number: $arg1
*/
let arg1 = process.argv[2];
arg1 = parseInt(arg1, 10);

if (Number.isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg1);
}
