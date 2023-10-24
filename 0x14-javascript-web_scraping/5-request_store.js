#!/usr/bin/node

/**
 *  gets the contents of a webpage and stores it in a file.
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 */

const { writeFile } = require('fs/promises');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    writeFile(fileName, body, { encoding: 'utf-8' })
      .catch(err => {
        console.log(err);
      });
  }
});
