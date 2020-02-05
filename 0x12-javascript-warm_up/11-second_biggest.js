#!/usr/bin/node
const arg = process.argv;
const array = [];
const array2 = [];

if (arg.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arg.length; i++) {
    array.push(Number(arg[i]));
  }
  for (let j = 0; j < array.length; j++) {
    if (array[j] !== Math.max(...array)) {
      array2.push(array[j]);
    }
  }
  console.log(Math.max(...array2));
}
