'use strict';

var numbers = [7, 5, 8, -1, 2, -10];
// Write a function that returns the minimal element
// in an array (your own min function)

function getMin(input) {
  return Math.min.apply(null, input);
}
console.log(getMin(numbers));

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply
