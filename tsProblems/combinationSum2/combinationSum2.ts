export const combinationSum2 = (
  candidates: number[],
  target: number,
  currTotal = 0,
  currCombo: number[] = [],
  combos: number[][] = []
): number[][] | number[] => {
  if (currTotal > target) {
    return [];
  }

  for (let i = 0; i < candidates.length; i++) {
    if (
      candidates.includes(target - currTotal) &&
      !combos.includes([...currCombo].sort())
    ) {
      // element is in array
      return [target - currTotal, ...currCombo];
    }
    const modifiedCombo = [...currCombo, candidates[i]];
    combos.push(
      [
        ...(combinationSum2(
          candidates.slice(0, i).concat(candidates.slice(i + 1)),
          target - candidates[i],
          currTotal + candidates[i],
          modifiedCombo,
          [...combos]
        ) as number[]),
      ].sort()
    );
  }
  return combos.filter((e) => e.length > 0);
};

console.log(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8));
