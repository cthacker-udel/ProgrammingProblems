export function isDuplicate(arr: any[], keyValue: any[]): boolean {
  return arr.filter((e) => e === keyValue).length > 0;
}

export function duplicated(arr: any[], keys: string[]): any[] {
  const dupeResults = {};
  arr.forEach((eachObj) => {});
}

const objs = [
  { x: 1, y: 1 },
  { x: 2, y: 2 },
  { x: 1, z: 1 },
  { x: 1, y: 1, z: 3 },
];
const keys = ["x", "y"];

console.log(
  duplicated(
    objs.map((x) => Object.assign({}, x)),
    keys.slice()
  )
);
