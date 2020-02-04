#!/usr/bin/node
let y = process.argv[2];

if (isNaN(y)) {
  y = 1;
} else {
  y = parseInt(y);
}
function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}

console.log(factorial(y));
