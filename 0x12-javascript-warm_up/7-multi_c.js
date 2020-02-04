#!/usr/bin/node
const string = 'C is fun';
const command = process.argv;
let number = command[2];

if (number == null) {
  console.log('Missing number of occurrences');
}
while (number > 0) {
  console.log(string);
  number--;
}
