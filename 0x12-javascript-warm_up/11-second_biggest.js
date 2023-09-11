#!/usr/bin/node
const args = process.argv.slice(2, process.argv.length);
let sec;
if (args.length <= 3) console.log(0);
else {
  sec = args.map(arg => parseInt(arg)).sort((a, b) => b - a)[1];
  console.log(sec);
}
