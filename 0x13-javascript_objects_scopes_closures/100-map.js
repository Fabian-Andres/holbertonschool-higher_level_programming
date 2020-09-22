#!/usr/bin/node
/**
 * Script that imports an array and computes a new array
 */
const list = require('./100-data').list;
console.log(list);
const list2 = list.map((el, index) => el * index);
console.log(list2);
