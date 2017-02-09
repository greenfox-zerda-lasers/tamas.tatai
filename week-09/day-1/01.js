'use strict';

const http = require('http');

const server = http.createServer(function cServ(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Request: ' + req.url + '\n' + 'Date: ' + new Date());
});


server.listen(3000, '127.0.0.1');
