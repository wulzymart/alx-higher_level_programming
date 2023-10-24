#!/usr/bin/node

/**
 * computes the number of tasks completed by user id.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        completed[task.userId] ? completed[task.userId]++ : completed[task.userId] = 1;
      }
    }
    console.log(completed);
  }
});
