'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function get(request, response) {
  response.send('get lost');
});

exampleApp.post('/', function post(request, response) {
  response.send('post lost');
});

exampleApp.listen(3000);
