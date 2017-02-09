'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function oddsEvens(inputList) {
  var returnList = [];
  for (var i = 0; i < inputList.length; i++) {
    if (inputList[i] % 2 === 1) {
      returnList.push(inputList[i]);
    }
  }
  return returnList;
}
console.log(oddsEvens(numbers));
