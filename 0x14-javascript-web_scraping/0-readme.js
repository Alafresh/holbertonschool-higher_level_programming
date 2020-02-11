#!/usr/bin/node
const path = process.argv[2];
const fs = require('fs');

fs.readFile(path, { encoding: 'utf-8' }, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
