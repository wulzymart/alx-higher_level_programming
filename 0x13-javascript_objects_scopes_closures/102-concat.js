#!/usr/bin/node
/**
 * script that concats 2 files.
 */
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
if (!fileC) process.exit(1);
const { readFile, writeFile } = require('fs');
readFile(fileA, { encoding: 'utf-8' }, (err, fileAContent) => {
  if (err) {
    console.log(err);
    return;
  }
  readFile(fileB, { encoding: 'utf-8' }, (err, fileBContent) => {
    if (err) {
      console.log(err);
      return;
    }
    writeFile(fileC, fileAContent + fileBContent, { encoding: 'utf-8' }, () => {});
  });
});
