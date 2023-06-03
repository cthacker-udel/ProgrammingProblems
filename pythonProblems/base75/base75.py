BASE_75 = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "!",
    "#",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    ",",
    ".",
    "/",
    ":",
]


def b75encode(orig: bytes) -> bytes:
    chunks = []
    sub_chunk = []
    appended_bytes = 0
    for each_byte in orig:
        sub_chunk.append(each_byte)
        if len(sub_chunk) == 7:
            chunks.append(sub_chunk)
            sub_chunk = []
    if len(sub_chunk) > 0:
        appended_bytes = 7 - len(sub_chunk)
        while len(sub_chunk) < 7:
            sub_chunk.append(0)
        chunks.append(sub_chunk)
        sub_chunk = []

    for ind, element in enumerate(chunks):
        # Convert chunk to massive binary number
        cloned_arr = element[:]
        for cloned_ind, cloned_element in enumerate(cloned_arr):
            print(type(cloned_element))
            cloned_arr[cloned_ind] = cloned_element % 75
        chunks[ind] = cloned_arr[:]

    print(chunks)


def b75decode(orig: bytes) -> bytes:
    print(orig)


if __name__ == "__main__":
    original = b"Simple text."
    encoded = b"Xh&1*IqZjg2gKO:a&E2"
    b75encode(original)
    b75decode(encoded)
