#!/usr/bin/node
const argv = process.argv;
let number = Number(argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
}
console.log(number);
