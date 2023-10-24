#!/usr/bin/node

/**
 * reads and prints the content of a file.
 */
const { readFile } = require('fs').promises;
const { argv } = process;

const fileName = argv[2];

readFile(fileName, { encoding: 'utf-8' })
  .then(content => {
    console.log(content);
  })
  .catch(error => {
    console.log(error);
  });
