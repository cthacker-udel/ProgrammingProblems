/**
 *
 * @param {number[]} arr
 */
function highestRank(arr) {
  occurrences = {};
  arr.forEach((e) => {
    if (e in occurrences) {
      occurrences[e] += 1;
    } else {
      occurrences[e] = 1;
    }
  });

  const sortedKeys = Object.entries(occurrences).sort((entry1, entry2) =>
    entry1[1] === entry2[1] ? entry1[0] - entry2[0] : entry1[1] - entry2[1]
  );
  return +sortedKeys.slice(-1)[0][0];
}

const arr1 = [12, 10, 8, 12, 7, 6, 4, 10, 12];
const arr2 = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10];
const arr3 = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10];

console.log(highestRank(arr1));
console.log(highestRank(arr2));
console.log(highestRank(arr3));
