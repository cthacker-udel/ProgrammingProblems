/**
 *
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @returns {number[]} The merged sorted array
 */
function mergeArrays(arr1, arr2) {
  return [...new Set(arr1.concat(arr2))].sort((e1, e2) => e1 - e2);
}

console.log(mergeArrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]));
