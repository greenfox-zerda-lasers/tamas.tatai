'use strict';

// create a function that when called alerts "I'm delayed" after 1 second

function Delayed() {
  window.alert("I'm delayed!");
}

setTimeout(Delayed, 1000);
