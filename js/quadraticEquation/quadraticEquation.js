/**
 * Calculates the root given the quadratic formula
 *
 * @param {number} a - A in the quadratic formula
 * @param {number} b - B in the quadratic formula
 * @param {number} c - C in the quadratic formula
 * @returns The root of the quadratic formula given a, b, and c
 */
const quadraticEquation = (a, b, c) => {
  const upperHalf = -1 * b + Math.sqrt(b * b - 4 * a * c);
  const lowerHalf = 2 * a;
  return upperHalf / lowerHalf;
};
