#!/usr/bin/node
/*
|    Script that prints the first
|    argument passed to it
*/
const lenValue = process.argv.length;

const argToPrint = process.argv[2];

if (lenValue < 3) {
  console.log('No argument');
} else {
  console.log(argToPrint);
}
