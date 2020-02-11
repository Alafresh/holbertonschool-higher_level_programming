#!/usr/bin/node
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body).characters;
    // console.log(typeof JSON.parse(body).characters);
    list.forEach(item => {
      request(item, function (err, response, body) {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
      });
    });
  }
});
