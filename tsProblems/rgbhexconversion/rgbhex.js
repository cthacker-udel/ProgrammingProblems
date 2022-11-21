"use strict";
exports.__esModule = true;
exports.rgb = void 0;
/**
 * converts rgb value to hex
 *
 * @param r - red value
 * @param g - green value
 * @param b - blue value
 */
var rgb = function (r, g, b) {
    return "".concat(Number.parseInt(r.toString(), 16)).concat(Number.parseInt(g.toString(), 16)).concat(Number.parseInt(b.toString(), 16));
};
exports.rgb = rgb;
console.log((0, exports.rgb)(0, 0, 0));
