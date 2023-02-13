"use strict";
exports.__esModule = true;
exports.seven = void 0;
function seven(m) {
  var steps = 0;
  var result = m;
  while (result > 99) {
    var mstr = result.toString();
    var last_digit = mstr.slice(-1);
    var remaining = mstr.slice(0, -1);
    result = Number.parseInt(remaining) - Number.parseInt(last_digit) * 2;
    steps++;
  }
  return [result, steps];
}
exports.seven = seven;
console.log(seven(477557101));
