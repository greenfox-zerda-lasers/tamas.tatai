'use strict';

// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)

var delayedLoop = function() {
  setTimeout(delayedLoop, 1500);
  console.log(mouseCoordinates);
}

var mouseCoordinates;

document.onmousemove = function(coordinate) {
  mouseCoordinates = coordinate.pageX + ", " + coordinate.pageY;
}

delayedLoop();
