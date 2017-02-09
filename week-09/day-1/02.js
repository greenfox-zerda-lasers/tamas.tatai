'use strict';

var express = require('express');

var app = express();

app.get('/', function cServe(req, res) {
  res.send('Request url: ' + req.url + '\n Method: ' + req.method + '\n Date: ' + new Date());
});

app.listen(3000);
