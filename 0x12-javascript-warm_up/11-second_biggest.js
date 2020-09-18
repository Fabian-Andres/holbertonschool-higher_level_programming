#!/usr/bin/node
/*
|   Script that searches the second biggest
|   integer in the list of arguments
*/
let args = process.argv;

args.splice(args[0], 2);
args = args.sort();
if (args[2] === undefined || args.length === 1) {
  console.log(0);
} else {
  console.log(args[args.length - 2]);
}
