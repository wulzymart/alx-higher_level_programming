#!/usr/bin/node
const args = process.argv;
const myNum = parseInt(args[2]);
let print;
let i, j;
if (!myNum) console.log('Missing size');
else {
  for (i = 0; i < myNum; i++) {
    print = '';
    for (j = 0; j < myNum; j++) {
      print += 'X';
    }
    console.log(print);
  }
}
