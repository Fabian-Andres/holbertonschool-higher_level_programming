#!/usr/bin/node
/*
|   Script that prints two arguments passed
|   to it, in the following format: “ is ”
*/
const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(arg1 + ' is ' + arg2);
