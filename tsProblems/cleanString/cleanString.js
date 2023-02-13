"use strict";
exports.__esModule = true;
exports.cleanString = void 0;
function cleanString(s) {
    var stack = [];
    for (var i = 0; i < s.length; i++) {
        switch (s[i]) {
            case "#": {
                stack = stack.slice(0, -1);
                break;
            }
            default: {
                stack.push(s[i]);
                break;
            }
        }
    }
    return stack.join("");
}
exports.cleanString = cleanString;
console.log(cleanString("abc##d######"));
console.log(cleanString("abc#d##c"));
