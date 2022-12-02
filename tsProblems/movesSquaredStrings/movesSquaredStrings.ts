export function vertMirror(strng: string) {
  return strng
    .split("\n")
    .map((eachStr: string) => eachStr.split("").reverse().join(""))
    .join("\n");
}

export function horMirror(strng: string) {
  return strng.split("\n").reverse().join("\n");
}

export function oper(fct: (s: string) => string, s: string) {
  return fct(s);
}
