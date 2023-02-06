def interpreter(tape: str) -> str:
    output = ""
    tape_value = 0
    for each_char in tape:
        if each_char == "?":
            tape_value += 1
        elif each_char == "!":
            output += chr(tape_value)
            tape_value = 0
