#!/usr/bin/node
/**
 *  function that returns the number of occurrences in a list:
 */
exports.nbOccurences = function (list, searchElement) {
  if (!list || !list.length || !searchElement) return 0;
  let count = 0;
  list.forEach(element => {
    element === searchElement && count++;
  });
  return count;
};
