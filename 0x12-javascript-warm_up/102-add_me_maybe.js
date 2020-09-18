#!/usr/bin/node
/*
|   Function that executes x times a function.
*/
exports.addMeMaybe = function (x, theFunction) {
    theFunction(++x);
}