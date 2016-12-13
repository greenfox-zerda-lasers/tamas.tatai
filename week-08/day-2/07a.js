'use strict';

// Embed the following file to a HTML document:
//  - https://www.flickr.com/photos/130463184@N04/15584243094 (use the embed feature)
//  - watch the DOMContentLoaded event also and change the background color of the page to red while the image is loading
//  - add a 'load' event to the window object that logs "loaded" when the image is downloaded and changes back the background color of the page to white


var changeToRed = function() {
  document.body.style.backgroundColor = 'red';
  console.log('lobab');
}

document.addEventListener('DOMContentLoaded', changeToRed);

var loadedLog = function() {
  document.body.style.backgroundColor = 'white';
  console.log('Loaded!');
}

window.addEventListener('load', loadedLog);
