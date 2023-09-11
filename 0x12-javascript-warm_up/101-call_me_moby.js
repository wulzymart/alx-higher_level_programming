#!/usr/bin/node
function callMeMoby (x, theFunction) {
  if (!x || !theFunction) return;
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
}
module.exports = { callMeMoby };
