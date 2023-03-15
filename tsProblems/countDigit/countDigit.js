"use strict";
exports.__esModule = true;
exports.countDigit = void 0;
function countDigit(number, digit, base, fromBase) {
    var convertedNumber = Number.parseInt(number, fromBase).toString(base);
    return convertedNumber.split("").filter(function (e) { return e === digit; }).length;
}
exports.countDigit = countDigit;
console.log(countDigit("10", "a", 11, 10));
