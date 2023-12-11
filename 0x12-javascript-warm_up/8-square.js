#!/usr/bin/node
const argv = process.argv;
const size = Number(argv[2]);
if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size).trimEnd());
  }
} else console.log('Missing size');
