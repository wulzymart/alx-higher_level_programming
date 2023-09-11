#!/usr/bin/node
const args = process.argv;
const length = args.length;
let max;
let sec;
if (args.length <= 3) console.log(0);
else {
  max = parseInt(args[2]);
  for (let i = 3; i < length; i++) {
    const current = parseInt(args[i]);
    if (current > max) {
      sec = max;
      max = current;
    } else if (current > sec) {
      sec = current;
    }
  }
  console.log(sec);
}
