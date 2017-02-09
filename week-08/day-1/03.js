'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets(consumption) {
  this.consumption = consumption;
  this.fuel = 0;
  this.launches = 0;
}

Rockets.prototype.fill = function(fuel) {
  this.fuel += fuel;
  // return this.fuel
}

Rockets.prototype.launch = function() {
  if (this.fuel >= this.consumption) {
    this.launches++;
    this.fuel -= this.consumption;
  } else {
    return ('refill that bitch!');
  }
}

var spaceRocket = new Rockets(5);
spaceRocket.fill(3);
spaceRocket.launch();
console.log(spaceRocket.launches);
console.log(spaceRocket.fuel);
