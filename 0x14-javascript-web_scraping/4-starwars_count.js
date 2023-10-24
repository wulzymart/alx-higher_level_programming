#!/usr/bin/node

/**
 * prints the number of movies where the character “Wedge Antilles” is present
 * The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const count = 0;
    const movies = JSON.parse(body).results;
    const countCharcter = movies.reduce((acc, curr) => {
      return curr.characters.map(url => url.split('/')[5]).includes('18') ? acc + 1 : acc;
    }, count);
    console.log(countCharcter);
  }
});
