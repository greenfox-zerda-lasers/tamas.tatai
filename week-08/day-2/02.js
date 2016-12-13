'use strict';

// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout

function Starter() {
  console.log('Delayed!');
}

var setTimer = setTimeout(Starter, 3000);

var button = document.createElement('button');
document.body.appendChild(button);
button.innerHTML = 'Button';

var stopTimer = function() {
  clearTimeout(setTimer);
  alert('Timer stopped!');
}

button.addEventListener('click', stopTimer);
