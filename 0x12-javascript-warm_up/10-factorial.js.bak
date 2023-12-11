#!/usr/local/bin/node
const { argv } = require("node:process");
const number = Number(argv[2]);
function factorial(x) {
  if (x <= 1 || isNaN(x)) {
    return 1;
  }
  return x * factorial(x - 1);
}
console.log(factorial(number));
