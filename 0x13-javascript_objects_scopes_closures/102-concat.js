#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const a = fs.readFileSync(argv[2], 'utf8');
const b = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(process.argv[4], a + b);
