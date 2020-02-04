#!/usr/bin/node
const square = 'X';
const size = process.argv[2];

if (process.argv.length <= 2) {
  console.log('Missing size');
} else if (isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  console.log(square.repeat(size));
}
