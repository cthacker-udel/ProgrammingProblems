"use strict";
exports.__esModule = true;
exports.nbMonths = void 0;
function nbMonths(startPriceOld, startPriceNew, savingPerMonth, percentLossByMonth) {
    var months = 0;
    var currentSavings = 0;
    var tmpStartPriceOld = startPriceOld; // avoid mutating
    var tmpStartPriceNew = startPriceNew;
    while (tmpStartPriceNew - (currentSavings + tmpStartPriceOld) > 0) {
        months++;
        if (months > 0 && months % 2 == 0) {
            percentLossByMonth += 0.5;
        }
        currentSavings += savingPerMonth;
        tmpStartPriceOld -= tmpStartPriceOld * (percentLossByMonth / 100);
        tmpStartPriceNew -= tmpStartPriceNew * (percentLossByMonth / 100);
    }
    var currTotal = currentSavings + tmpStartPriceOld;
    return [months, Math.round(currTotal - tmpStartPriceNew)];
}
exports.nbMonths = nbMonths;
console.log(nbMonths(12000, 8000, 1000, 1.5));
console.log(nbMonths(2000, 8000, 1000, 1.5));
