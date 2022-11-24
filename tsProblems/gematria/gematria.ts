export function gematria(str: string): number {
  const letter_dict: { [key: string]: number } = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
    f: 6,
    g: 7,
    h: 8,
    i: 9,
    k: 10,
    l: 20,
    m: 30,
    n: 40,
    o: 50,
    p: 60,
    q: 70,
    r: 80,
    s: 90,
    t: 100,
    u: 200,
    x: 300,
    y: 400,
    z: 500,
    j: 600,
    v: 700,
    w: 900,
  };

  return str
    .toLowerCase()
    .split("")
    .map((eachLetter) =>
      letter_dict[eachLetter] ? letter_dict[eachLetter] : 0
    )
    .reduce((e1, e2) => e1 + e2, 0);
}
