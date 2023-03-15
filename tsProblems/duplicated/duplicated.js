"use strict";
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
exports.__esModule = true;
exports.duplicated = exports.isDuplicate = void 0;
function isDuplicate(arr, keyValue) {
    return arr.filter(function (e) { return e === keyValue; }).length > 0;
}
exports.isDuplicate = isDuplicate;
function duplicated(arr, keys) {
    var dupes = new Set();
    var formattedArr = arr.map(function (eachObj) {
        return keys.map(function (eachKey) { return eachObj[eachKey]; });
    });
    console.log(formattedArr);
    formattedArr.forEach(function (eachObj, ind) {
        if (!dupes.has(arr[ind]) && isDuplicate(arr, eachObj)) {
            dupes.add(arr[ind]);
        }
    });
    return __spreadArray([], __read(dupes), false);
}
exports.duplicated = duplicated;
var objs = [
    { x: 1, y: 1 },
    { x: 2, y: 2 },
    { x: 1, z: 1 },
    { x: 1, y: 1, z: 3 },
];
var keys = ["x", "y"];
console.log(duplicated(objs.map(function (x) { return Object.assign({}, x); }), keys.slice()));
