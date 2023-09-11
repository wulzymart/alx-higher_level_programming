#!/usr/bin/node
const args = process.argv;
let myNum = parseInt(args[2]);
if (!myNum) console.log('Missing number of occurrences');
else {
  while (myNum > 0) {
    console.log('C is fun');
    myNum--;
  }
}
