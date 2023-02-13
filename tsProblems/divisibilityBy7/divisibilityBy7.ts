export function seven(m: number): number[] {
  let steps = 0;
  let result = m;
  while (result > 99) {
    const mstr = result.toString();
    const last_digit = mstr.slice(-1);
    const remaining = mstr.slice(0, -1);
    result = Number.parseInt(remaining) - Number.parseInt(last_digit) * 2;
    steps++;
  }
  return [result, steps];
}

console.log(seven(1021));
