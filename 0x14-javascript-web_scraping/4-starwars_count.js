#!/usr/bin/node
/**
 * 
 */
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body).results;
    let count = 0;
    for (var key in res) {
      if (res[key].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
