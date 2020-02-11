#!/usr/bin/node

const file = process.argv[3];
const url = process.argv[2];
const request = require('request');
const fs = require('fs');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
