export function spoonerize(words: string): string {
  const splitWords: string[] = words.split(" ");
  return splitWords.length === 3
    ? `${splitWords[2][0]}${splitWords[0].substring(1)} ${splitWords[1]} ${
        splitWords[0][0]
      }${splitWords[2].substring(1)}`
    : `${splitWords[1][0]}${splitWords[0].substring(1)} ${
        splitWords[0][0]
      }${splitWords[1].substring(1)}`;
}

spoonerize("not picking");
