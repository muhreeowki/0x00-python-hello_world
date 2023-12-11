#!/usr/bin/node
const argv = process.argv;
const numbers = argv.map((val) => Number(val)).filter((val) => !isNaN(val));
numbers.splice(numbers.indexOf(Math.max(...numbers)), 1);
console.log(Math.max(...numbers));
