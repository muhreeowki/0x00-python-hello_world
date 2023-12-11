#!/usr/local/bin/node
const fs = require("fs");
const { argv } = require("node:process");

fs.readFile(argv[2], (err, data) => {
  if (err) throw err;
  fs.writeFile(argv[4], data, (err) => {
    if (err) throw err;
  });
});

fs.readFile(argv[3], (err, data) => {
  if (err) throw err;
  fs.appendFile(argv[4], data, (err) => {
    if (err) throw err;
  });
});
