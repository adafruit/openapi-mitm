const request = require('request');
const https = require('https');
const http = require('http');
const url = require('url');
const fs = require('fs');

const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

https.createServer(options, (req, res) => {
  console.log(`[${req.method}]: ${req.url}`);
  req.pipe(request(req.url)).pipe(res);
}).listen(8889);

http.createServer((req, res) => {
  console.log(`[${req.method}]: ${req.url}`);
  req.pipe(request(req.url)).pipe(res);
}).listen(8888);
