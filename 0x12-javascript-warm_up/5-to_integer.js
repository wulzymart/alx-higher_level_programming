#!/usr/bin/node
const args = process.argv;
const myNum = parseInt(args[2]);
if (myNum) console.log(`My number: ${myNum}`);
else console.log('Not a number');
