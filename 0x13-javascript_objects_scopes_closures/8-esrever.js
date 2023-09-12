#!/usr/bin/node
/**
 * function that returns the reversed version of a list:
 */
exports.esrever = function (list) {
  if (!list || list.length === 0) return list;
  const reversedList = [];
  const length = list.length;
  let i;
  for (i = length - 1; i >= 0; i--) reversedList.push(list[i]);
  return reversedList;
};
