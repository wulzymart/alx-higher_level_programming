#!/usr/bin/node
/**
 *  function that prints the number of arguments already printed and the new argument value.
 */

let printed = 0;
exports.logMe = function (item) {
  if (!item) return;
  console.log(`${printed}: ${item}`);
  printed++;
};
