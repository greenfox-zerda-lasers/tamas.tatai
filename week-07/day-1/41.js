'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10].reduce(sumIt, 0);
// write your own sum function

function sumIt(a, b) {
  return a + b;
}
console.log(numbers);
