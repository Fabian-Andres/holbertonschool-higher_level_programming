#!/usr/bin/node
/*
|   Script that prints computes and prints a factorial
*/
let arg1 = process.argv[2];
arg1 = parseInt(arg1, 10);

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (Number.isNaN(arg1)) {
  console.log(1);
} else {
  console.log(factorial(arg1));
}
