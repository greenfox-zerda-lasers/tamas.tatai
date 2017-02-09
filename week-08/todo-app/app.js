'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var input = document.querySelector('.input');
var button = document.querySelector('.button');
var checkbox = document.querySelectorAll('.checkbox');
var trash = document.querySelector('.ion-ios-trash-outline');


function getTodos(callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url);
  xhr.send();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      var req = JSON.parse(xhr.response);
      console.log(callback(xhr));
    };
  };
};

getTodoItems(getTodoList);

function getTodoList(res) {
  res.forEach(function(e) {
    var newItem = document.createElement('p');
    newItem.innerText = e.id + '. ' + e.text;
    newItem.setAttribute('id', e.id)
    document.body.appendChild(newItem);
  });
}

