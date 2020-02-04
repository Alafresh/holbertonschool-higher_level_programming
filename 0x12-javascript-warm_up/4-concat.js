#!/usr/bin/node
const command = process.argv;
if (command[2] == null) {
  console.log(command[2] + ' is ' + command[2]);
} else {
  console.log(command[2] + ' is ' + command[3]);
}
