export function cleanString(s: string): string {
  let stack: string[] = [];
  for (let i = 0; i < s.length; i++) {
    switch (s[i]) {
      case "#": {
        stack = stack.slice(0, -1);
        break;
      }
      default: {
        stack.push(s[i]);
        break;
      }
    }
  }
  return stack.join("");
}

console.log(cleanString("abc##d######"));
console.log(cleanString("abc#d##c"));
