"use strict";
exports.__esModule = true;
exports.chooseBestSum = void 0;
/**
 *
 *
 * @param maxLimit - The summation limit, which controls the maximum distance we can travel
 * @param numberOfTowns - The minimum number of towns we can visit
 * @param distances - The list of distances we can use to contribute to the sum
 */
function chooseBestSum(maxLimit, numberOfTowns, distances) {
    // sort the distances, pick the largest, check if that is included within the array,  and continue until we have a summation
    distances.sort(function (a, b) { return a - b; });
    // start with largest (end)
    var max_sum = -Infinity;
    for (var i = distances.length - 1; i >= 0; i--) {
        // grab largest distance, compute sum\
        var distancesClone = distances.slice();
        var sumCount = 1;
        var sum = distancesClone[i];
        var diff = maxLimit - distancesClone[i];
        distancesClone.splice(i, 1);
        var j = distancesClone.length - 1;
        while (sumCount < numberOfTowns && j >= 0) {
            if (distancesClone.indexOf(diff - distancesClone[j]) !== -1 || diff - distancesClone[j] === 0) {
                sum += distancesClone[j];
                sumCount++;
                diff -= distancesClone[j];
                distancesClone.splice(j, 1);
            }
            else {
                j--;
            }
        }
        if (sumCount == numberOfTowns && sum <= maxLimit && sum >= max_sum) {
            max_sum = sum;
        }
    }
    return max_sum !== -Infinity ? max_sum : null;
}
exports.chooseBestSum = chooseBestSum;
console.log(chooseBestSum(163, 3, [50]));
console.log(chooseBestSum(163, 3, [50, 55, 56, 57, 58]));
console.log(chooseBestSum(230, 3, [91, 74, 73, 85, 73, 81, 87]));
