"use strict";
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
exports.combinationSum2 = void 0;
var combinationSum2 = function (candidates, target, currTotal, currCombo, combos) {
    if (currTotal === void 0) { currTotal = 0; }
    if (currCombo === void 0) { currCombo = []; }
    if (combos === void 0) { combos = []; }
    if (currTotal > target) {
        return [];
    }
    for (var i = 0; i < candidates.length; i++) {
        if (candidates.includes(target - currTotal) &&
            !combos.includes(__spreadArray([], currCombo, true).sort())) {
            // element is in array
            return __spreadArray([target - currTotal], currCombo, true);
        }
        var modifiedCombo = __spreadArray(__spreadArray([], currCombo, true), [candidates[i]], false);
        combos.push(__spreadArray([], (0, exports.combinationSum2)(candidates.slice(0, i).concat(candidates.slice(i + 1)), target - candidates[i], currTotal + candidates[i], modifiedCombo, __spreadArray([], combos, true)), true).sort());
    }
    return combos.filter(function (e) { return e.length > 0; });
};
exports.combinationSum2 = combinationSum2;
console.log((0, exports.combinationSum2)([10, 1, 2, 7, 6, 1, 5], 8));
