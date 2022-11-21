
def shifted_diff(first: str, second: str) -> int:
    for i in range(len(first)):
        if f"{first[-i:]}{first[:-i]}" == second:
            return i
    return -1


if __name__ == '__main__':
    f = "Esham"
    s = "Esham"
    print(shifted_diff(f, s))