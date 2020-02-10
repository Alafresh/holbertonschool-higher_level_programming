#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const size = list.length;
  let count = 0;
  for (let i = 0; i < size; i++) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }
  return count;
};
