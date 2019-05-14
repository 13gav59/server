const express = require('express');

const app = express();

const PORT = 8080;

app.get('/', function(req, res) {
  console.log("payload recieved");
});

app.listen(PORT, () => {
  console.log("webserver running");
});
