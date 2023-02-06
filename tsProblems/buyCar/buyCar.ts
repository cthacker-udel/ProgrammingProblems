export function nbMonths(
  startPriceOld: number,
  startPriceNew: number,
  savingPerMonth: number,
  percentLossByMonth: number
): number[] {
  let months = 0;
  let currentSavings = 0;
  let tmpStartPriceOld = startPriceOld; // avoid mutating
  let tmpStartPriceNew = startPriceNew;
  while (tmpStartPriceNew - (currentSavings + tmpStartPriceOld) > 0) {
    months++;
    if (months > 0 && months % 2 == 0) {
      percentLossByMonth += 0.5;
    }
    currentSavings += savingPerMonth;
    tmpStartPriceOld -= tmpStartPriceOld * (percentLossByMonth / 100);
    tmpStartPriceNew -= tmpStartPriceNew * (percentLossByMonth / 100);
  }
  let currTotal = currentSavings + tmpStartPriceOld;
  return [months, Math.round(currTotal - tmpStartPriceNew)];
}

console.log(nbMonths(12000, 8000, 1000, 1.5));
console.log(nbMonths(2000, 8000, 1000, 1.5));
