#!/usr/local/bin/node

const initialDict = require("./101-data").dict;
const newDict = {};

for (let [key, value] of Object.entries(initialDict)) {
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}

console.log(newDict);
