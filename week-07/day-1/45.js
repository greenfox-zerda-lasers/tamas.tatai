'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortString(input) {
  var shortest = input[0];
  for (var i = 1; i < input.length; i++) {
    if (shortest.length > input[i].length) {
      shortest = input[i];
    }
  }
  return shortest;
}
console.log(shortString(names));
