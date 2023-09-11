#!/usr/bin/node
const args = process.argv;
const myNum = parseInt(args[2]);
function factorial (num) {
  if (!num || num <= 1) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(myNum));
