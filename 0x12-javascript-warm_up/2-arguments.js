#!/usr/bin/node
const args = process.argv.length;
if (args > 2) console.log(`Argument${(args > 3 ? 's' : '')} found`);
else console.log('No argument');
