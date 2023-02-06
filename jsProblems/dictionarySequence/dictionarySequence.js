function* letters() {
  yield* "abcdefghijklmnopqrstuvwxyz";
  yield* "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  while (true) {
    console.log(yield* letters());
  }
}

let iter = letters();
for (let i = 0; i < 109; i++) {
  console.log(iter.next().value);
}
