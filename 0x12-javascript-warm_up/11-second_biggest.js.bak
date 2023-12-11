#!/usr/local/bin/node
const { argv } = require("node:process");
const numbers = argv.map((val) => Number(val)).filter((val) => !isNaN(val));
numbers.splice(numbers.indexOf(Math.max(...numbers)), 1);
console.log(Math.max(...numbers));
