#!/usr/bin/node
/*
|    Script that prints the first
|    argument passed to it
*/
const argToPrint = process.argv[2];

if (argToPrint === undefined) {
  console.log('No argument');
} else {
  console.log(argToPrint);
}
