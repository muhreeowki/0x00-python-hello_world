#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]);
function factorial(x) {
  if (x <= 1 || isNaN(x)) {
    return 1;
  }
  return x * factorial(x - 1);
}
console.log(factorial(number));
