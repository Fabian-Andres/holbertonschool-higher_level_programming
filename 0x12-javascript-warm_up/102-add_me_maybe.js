#!/usr/bin/node
/*
|   Function that increments and calls a function.
*/
exports.addMeMaybe = function (x, theFunction) {
    theFunction(++x);
}