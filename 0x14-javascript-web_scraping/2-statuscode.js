#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
  console.log('code:', response && response.statusCode);
  if (error) {
    console.log('code:', error.message);
  }
});
