#!/usr/bin/node

/**
 * prints the title of a Star Wars movie where the episode number matches a given integer
 * The first argument is the movie ID
 */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (err, res) => {
  if (err) console.log(err);
  else {
    const resObj = JSON.parse(res.body);
    console.log(resObj.title);
  }
});
