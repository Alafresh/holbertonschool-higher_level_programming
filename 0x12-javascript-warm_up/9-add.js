#!/usr/bin/node
const x = process.argv[2];
const y = process.argv[3];

function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
add(x, y);
