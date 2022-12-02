function isExactlyThree(n) {
  let ct = 1;
  for (let i = 2; i <= Math.ceil(Math.sqrt(n)) + 1; i++) {
    if (ct > 3) {
      return false;
    }
    if (n % i == 0) {
      ct++;
    }
  }
  return ct == 3;
}
