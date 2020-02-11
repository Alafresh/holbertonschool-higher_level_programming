#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const tasks = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0
};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body);
    for (let i = 0; i < list.length; i++) {
      if (list[i].completed === true) {
        tasks[list[i].userId] += 1;
      }
    }
    console.log(tasks);
  }
});
