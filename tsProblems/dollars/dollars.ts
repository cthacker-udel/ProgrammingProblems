export const dollars = (amounts: string[]): boolean => {
  console.log(typeof amounts, amounts.constructor, JSON.stringify(amounts));

  const colorSet = new Set(amounts);
  return (
    colorSet.size === 1 &&
    (colorSet.has("red") || colorSet.has("blue") || colorSet.has("green"))
  );
};

console.log(dollars(["red", "red", "purple"]));
