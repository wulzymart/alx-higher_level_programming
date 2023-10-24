#!/usr/bin/node
/**
 * prints the title of a Star Wars movie where the episode number matches a given integer
 * The first argument is the movie ID
 */

const request = require('request');
const { promisify } = require('util');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, async (err, res, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    const req = promisify(request.get);
    for (const url of characters) {
      await req(url)
        .then((res) => {
          console.log(JSON.parse(res.body).name);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
});
