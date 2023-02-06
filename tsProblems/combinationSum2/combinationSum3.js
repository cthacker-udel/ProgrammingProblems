/**
 *
 * @param {number[]} candidates
 * @param {number[]} target
 */
function combinationSum2(candidates, target) {
  // Choice, choosing a number to include in the combination
  // Constraint, must sum <= target, and numbers can only be used once, so removal of choice in recursive call will achieve that desired result
  // Goal, find combination that sums to target
  // Must at least have a rejection, and accept function

  let candidatesSum = candidates.reduce((e1, e2) => e1 + e2, 0);
  if (candidatesSum < target) {
    return [];
  }

  /**
   *
   * @param {number} target
   * @param {number[]} decision
   * @returns
   */
  function acceptDecision(target, decision) {
    return decision.reduce((e1, e2) => e1 + e2, 0) === target;
  }

  /**
   *
   * @param {number[]} decision
   * @param {number} target
   */
  function isValidDecision(decision, target) {
    return decision.reduce((e1, e2) => e1 + e2, 0) <= target;
  }

  // choose
  // validate
  // unchoose

  const combos = [];
  const exploredSubCombos = [];

  /**
   *
   * @param {number[]} candidates
   * @param {number} target
   * @param {number[]} currentCombo
   * @param {number[]} combos
   */
  function combinationRecursion(
    candidates,
    target,
    combos,
    exploredSubCombos,
    currentCombo = []
  ) {
    for (let i = 0; i < candidates.length; i++) {
      currentCombo.push(candidates[i]);
      if (
        isValidDecision(currentCombo, target) &&
        !exploredSubCombos.includes(JSON.stringify(currentCombo))
      ) {
        exploredSubCombos.push(JSON.stringify(currentCombo));
        combinationRecursion(
          candidates.slice(0, i).concat(candidates.slice(i + 1)),
          target,
          combos,
          exploredSubCombos,
          currentCombo
        );
      }

      currentCombo.pop();
    }
    if (acceptDecision(target, currentCombo)) {
      let sortedCombo = [...currentCombo].sort();
      if (!combos.includes(sortedCombo)) {
        combos.push(sortedCombo);
      }
    }
  }

  combinationRecursion(candidates, target, combos, exploredSubCombos);
  return [...new Set([...combos].map((e) => JSON.stringify(e)))].map((e) =>
    JSON.parse(e)
  );
}

var v = combinationSum2(
  [
    29, 19, 14, 33, 11, 5, 9, 23, 23, 33, 12, 9, 25, 25, 12, 21, 14, 11, 20, 30,
    17, 19, 5, 6, 6, 5, 5, 11, 12, 25, 31, 28, 31, 33, 27, 7, 33, 31, 17, 13,
    21, 24, 17, 12, 6, 16, 20, 16, 22, 5,
  ],
  28
);

console.log(v);
var w = combinationSum2(
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  27
);
console.log(w);
var x = combinationSum2([10, 1, 2, 7, 6, 1, 5], 8);
console.log(x);
var y = combinationSum2([2, 5, 2, 1, 2], 5);
console.log(y);
var z = combinationSum2([4, 2, 5, 2, 5, 3, 1, 5, 2, 2], 9);
console.log(z);
let b = [1];
console.log(combinationSum2(b, 1));
let a = [
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
];
console.log(combinationSum2(a, 30));
