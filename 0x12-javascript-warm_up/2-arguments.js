#!/usr/bin/node
/*
|    Script that prints a message depending
|    of the number of arguments passed
*/
const lenValue = process.argv.length;

if (lenValue < 3) {
  console.log('No argument');
} else if (lenValue === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
