export function countDigit(
  number: string,
  digit: string,
  base: number,
  fromBase: number
): number {
  const convertedNumber = Number.parseInt(number, fromBase).toString(base);
  return convertedNumber.split("").filter((e) => e === digit).length;
}

console.log(countDigit("10", "a", 11, 10));
