#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  if (!number || !theFunction) return;
  theFunction(number + 1);
}
module.exports = { addMeMaybe };
