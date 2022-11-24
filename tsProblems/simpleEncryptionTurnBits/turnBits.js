"use strict";
exports.__esModule = true;
exports.decrypt = exports.encrypt = exports.flipBit = void 0;
function flipBit(bit) {
    return bit === "0" ? "1" : "0";
}
exports.flipBit = flipBit;
function encrypt(text) {
    var _a, _b, _c, _d;
    var allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .";
    var doesContainIllegalChars = text
        .split("")
        .some(function (eachChar) { return !allowedChars.includes(eachChar); });
    if (doesContainIllegalChars) {
        throw new Error("Contains illegal chars");
    }
    else {
        var splitStr = text.split("");
        var binValues = [];
        for (var _i = 0, splitStr_1 = splitStr; _i < splitStr_1.length; _i++) {
            var eachStr = splitStr_1[_i];
            var convertedChar = allowedChars
                .indexOf(eachStr)
                .toString(2)
                .padStart(6, "0");
            binValues.push(convertedChar);
        }
        for (var i = 0; i < binValues.length; i++) {
            var firstBin = binValues[i].split("");
            // Step 1
            if (i < binValues.length - 1) {
                var forwardBin = binValues[i + 1].split("");
                _a = [forwardBin[0], firstBin[4]], firstBin[4] = _a[0], forwardBin[0] = _a[1];
            }
            // Step 2
            firstBin[1] = flipBit(firstBin[1]);
            firstBin[3] = flipBit(firstBin[3]);
            // Step 3
            _b = [
                firstBin[3],
                firstBin[4],
                firstBin[5],
                firstBin[0],
                firstBin[1],
                firstBin[2],
            ], firstBin[0] = _b[0], firstBin[1] = _b[1], firstBin[2] = _b[2], firstBin[3] = _b[3], firstBin[4] = _b[4], firstBin[5] = _b[5];
            // Step 4
            for (var i_1 = 0; i_1 < firstBin.length - 1; i_1 += 2) {
                _c = [firstBin[i_1 + 1], firstBin[i_1]], firstBin[i_1] = _c[0], firstBin[i_1 + 1] = _c[1];
            }
            // Step 5
            firstBin.reverse();
            // Step 6
            _d = [firstBin[2], firstBin[0]], firstBin[0] = _d[0], firstBin[2] = _d[1];
            binValues[i] = firstBin.join("");
        }
        for (var _e = 0, binValues_1 = binValues; _e < binValues_1.length; _e++) {
            var eachBinValue = binValues_1[_e];
            console.log("bin = ", eachBinValue);
            var indexValue = Number.parseInt(eachBinValue, 2);
            console.log("ind = ", indexValue);
            console.log(allowedChars[indexValue]);
        }
    }
    return "";
}
exports.encrypt = encrypt;
function decrypt(encryptedText) {
    return "";
}
exports.decrypt = decrypt;
encrypt("B9");
