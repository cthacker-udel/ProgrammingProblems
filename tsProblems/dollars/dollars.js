"use strict";
exports.__esModule = true;
exports.dollars = void 0;
var dollars = function (amounts) {
    console.log(typeof amounts, amounts.constructor, JSON.stringify(amounts));
    var colorSet = new Set(amounts);
    return (colorSet.size === 1 &&
        (colorSet.has("red") || colorSet.has("blue") || colorSet.has("green")));
};
exports.dollars = dollars;
console.log((0, exports.dollars)(["red", "red", "purple"]));
