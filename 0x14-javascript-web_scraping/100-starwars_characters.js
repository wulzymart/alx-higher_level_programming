#!/usr/bin/node
/**
 * prints the title of a Star Wars movie where the episode number matches a given integer
 * The first argument is the movie ID
 */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (const url of characters) {
      request.get(url, (err, res, body) => {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
