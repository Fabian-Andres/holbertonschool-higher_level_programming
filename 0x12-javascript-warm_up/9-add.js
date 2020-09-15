#!/usr/bin/node
/*
|   Script that prints the addition of 2 integers
*/
let arg1 = process.argv[2];
let arg2 = process.argv[3];
arg1 = parseInt(arg1, 10);
arg2 = parseInt(arg2, 10);

function add (a, b) {
  return (a + b);
}

if (Number.isNaN(arg2)) {
  console.log(arg2);
} else {
  console.log(add(arg1, arg2));
}
