'use strict';

// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call

var delayedLoop = setInterval(logMovement, 1500);

var mouseCoordinates;

document.onmousemove = function(coordinate) {
  mouseCoordinates = coordinate.pageX + ", " + coordinate.pageY;
}

function logMovement() {
  console.log(mouseCoordinates);
}
