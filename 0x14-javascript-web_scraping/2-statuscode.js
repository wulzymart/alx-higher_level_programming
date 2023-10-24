#!/usr/bin/node
/**
 * display the status code of a GET request.
 * first argument is the URL to request (GET)
 * status code must be printed like this: code: <status code>
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) console.log(err);
  else console.log(`code: ${res.statusCode}`);
});
