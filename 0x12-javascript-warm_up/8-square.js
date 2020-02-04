#!/usr/bin/node
/*
    Print a square with the character #

    The size of the square must be the first argument
    of the program.
*/
const square = 'X';

if (process.argv.length <= 2) {
  console.log('Missing size');
}

if (typeof process.argv[2] === 'string') {
  console.log('Missing size');
}
const size = process.argv[2];

for (let i = 0; i < size; i++) {
  console.log(square.repeat(size));
}
