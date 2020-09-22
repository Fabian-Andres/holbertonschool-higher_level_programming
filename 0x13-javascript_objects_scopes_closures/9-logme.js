#!/usr/bin/node
/* Function that prints the number of arguments already printed and the new */
let nTime = 0;

exports.logMe = function (item) {
  console.log(nTime + ': ' + item);
  nTime += 1;
};
