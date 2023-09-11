#!/usr/bin/node
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);
function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
