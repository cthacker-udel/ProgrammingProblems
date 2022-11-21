/**
 * converts rgb value to hex
 *
 * @param r - red value
 * @param g - green value
 * @param b - blue value
 */
export const rgb = (r: number, g: number, b: number): string =>
  `${Number.parseInt(r.toString(), 16)}${Number.parseInt(
    g.toString(),
    16
  )}${Number.parseInt(b.toString(), 16)}`;

console.log(rgb(0, 0, 0));
