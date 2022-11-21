"use strict";
exports.__esModule = true;
exports.spoonerize = void 0;
function spoonerize(words) {
    var splitWords = words.split(" ");
    return splitWords.length === 3
        ? "".concat(splitWords[2][0]).concat(splitWords[0].substring(1), " ").concat(splitWords[1], " ").concat(splitWords[0][0]).concat(splitWords[2].substring(1))
        : "".concat(splitWords[2][0]).concat(splitWords[0].substring(1), " ").concat(splitWords[0][0]).concat(splitWords[2].substring(1));
}
exports.spoonerize = spoonerize;
spoonerize("not picking");
