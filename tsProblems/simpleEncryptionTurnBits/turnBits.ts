export function flipBit(bit: string): string {
  return bit === "0" ? "1" : "0";
}

export function encrypt(text: string): string {
  const allowedChars: string =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .";
  const doesContainIllegalChars = text
    .split("")
    .some((eachChar) => !allowedChars.includes(eachChar));
  if (doesContainIllegalChars) {
    throw new Error("Contains illegal chars");
  } else {
    const splitStr = text.split("");
    const binValues: string[] = [];
    for (const eachStr of splitStr) {
      const convertedChar = allowedChars
        .indexOf(eachStr)
        .toString(2)
        .padStart(6, "0");
      binValues.push(convertedChar);
    }
    for (let i = 0; i < binValues.length; i++) {
      const firstBin = binValues[i].split("");
      // Step 1
      if (i < binValues.length - 1) {
        const forwardBin = binValues[i + 1].split("");
        [firstBin[4], forwardBin[0]] = [forwardBin[0], firstBin[4]];
      }

      // Step 2
      firstBin[1] = flipBit(firstBin[1]);
      firstBin[3] = flipBit(firstBin[3]);

      // Step 3
      [
        firstBin[0],
        firstBin[1],
        firstBin[2],
        firstBin[3],
        firstBin[4],
        firstBin[5],
      ] = [
        firstBin[3],
        firstBin[4],
        firstBin[5],
        firstBin[0],
        firstBin[1],
        firstBin[2],
      ];

      // Step 4
      for (let i = 0; i < firstBin.length - 1; i += 2) {
        [firstBin[i], firstBin[i + 1]] = [firstBin[i + 1], firstBin[i]];
      }

      // Step 5
      firstBin.reverse();

      // Step 6
      [firstBin[0], firstBin[2]] = [firstBin[2], firstBin[0]];
      binValues[i] = firstBin.join("");
    }
    for (const eachBinValue of binValues) {
      console.log("bin = ", eachBinValue);
      const indexValue = Number.parseInt(eachBinValue, 2);
      console.log("ind = ", indexValue);
      console.log(allowedChars[indexValue]);
    }
  }
  return "";
}

export function decrypt(encryptedText: string): string {
  return "";
}

encrypt("B9");
