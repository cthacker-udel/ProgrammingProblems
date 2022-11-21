/**
 *
 * @param {Array<any>} arr - array with values
 * @param {any} value - value to search for
 * @returns
 */
// export const locate = (arr, value) => {
//   return arr
//     .flat(Number.POSITIVE_INFINITY)
//     .some((eachValue) => eachValue === value);
// };

/**
 *
 * @param {Array<any>} arr - array with values
 * @param {any} value - value to search for
 * @returns
 */
var locate = function (arr, value) {
  if (arr === undefined) {
    return false;
  }
  let found = false;
  for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "object") {
      // is array, recursively call
      found = found || locate(arr[i], value);
    } else if (arr[i] === value) {
      found = true;
      break;
    } else {
      found = false;
    }
  }
  return found;
};

let arr = ["two", "six", ["five", "seven"], "three,nine"];
let searchValue = "six";

console.log(locate(arr, searchValue));
