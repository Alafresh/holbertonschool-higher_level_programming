#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const tasks = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body);
    for (let i = 0; i < list.length; i++) {
      if (list[i].completed === true) {
        if (tasks[list[i].userId] === undefined) {
          tasks[list[i].userId] = 1;
        } else {
          tasks[list[i].userId] += 1;
        }
      }
    }
    console.log(tasks);
  }
});
