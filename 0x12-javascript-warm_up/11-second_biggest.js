#!/usr/local/bin/node
const argv = process.argv;
const numbers = argv.map((val) => Number(val)).filter((val) => !isNaN(val));
numbers.splice(numbers.indexOf(Math.max(...numbers)), 1);
const secondBiggest = Math.max(...numbers);
if (secondBiggest >= 0) console.log(secondBiggest);
else console.log(0);
