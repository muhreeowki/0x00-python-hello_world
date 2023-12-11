#!/usr/bin/node
const argv = process.argv;
try {
  console.log(`My number: ${Number(argv[2])}`);
} catch (error) {
  console.log('Not a number');
}
