#!/usr/bin/node
/**
 * Writes a sring to a file
 */

const { writeFile } = require('fs/promises');
const { argv } = process;

writeFile(argv[2], argv[3], { encoding: 'utf-8' })
  .catch(error => {
    console.log(error);
  });
