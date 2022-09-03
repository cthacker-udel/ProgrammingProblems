/**
 * Calculates the root given a, b, and c in the quadratic equation
 *
 * @param a - A in the quadratic equation
 * @param b - B in the quadratic equation
 * @param c - C in the quadratic equation
 * @returns The root value given a, b, and c in the quadratic equation
 */
const quadraticEquationFunc = (a: number, b: number, c: number): number => {
  const upperHalf: number = -b + Math.sqrt(b * b - 4 * a * c);
  const lowerHalf: number = 2 * a;
  return upperHalf / lowerHalf;
};
