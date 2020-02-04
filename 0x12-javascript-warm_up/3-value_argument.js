#!/usr/bin/node
const command = process.argv;
if (command[2] == null) {
  console.log('No argument');
} else {
  console.log(command[2]);
}
