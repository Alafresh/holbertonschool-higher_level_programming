#!/usr/bin/node
const command = process.argv;
const number = parseInt(command[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
