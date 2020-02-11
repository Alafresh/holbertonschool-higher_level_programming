#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j] === 'https://swapi.co/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
