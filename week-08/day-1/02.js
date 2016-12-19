'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(x, y) {
  this.x = x;
  this.y = y;
}

Rectangles.prototype.getArea = function() {
  return this.x * this.y;
}

Rectangles.prototype.getCircumference = function() {
  return 2 * (this.x + this.y);
}

var rect = new Rectangles(45, 43);
console.log(rect.getArea());
console.log(rect.getCircumference());
