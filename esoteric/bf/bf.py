def brain_luck(code, program_input):
    TAPE_LEN = 4000
    CODE_LEN = len(code)

    tape = [0] * TAPE_LEN
    bracket_idxs = {}
    tape_idx = 0
    code_idx = 0
    output = ""

    while code_idx < CODE_LEN:
        if code[code_idx] == ",":
            tape[tape_idx] = ord(program_input[0])
            program_input = program_input[1:]
        elif code[code_idx] == "+":
            tape[tape_idx] = (tape[tape_idx] + 1) % 256
        elif code[code_idx] == "-":
            tape[tape_idx] -= 1
            if tape[tape_idx] < 0:
                tape[tape_idx] = 255
        elif code[code_idx] == ">":
            tape_idx += 1
        elif code[code_idx] == "<":
            tape_idx -= 1
        elif code[code_idx] == ".":
            output += chr(tape[tape_idx])
        elif code[code_idx] == "[":
            if code_idx in bracket_idxs and code[code_idx] == 0:
                code_idx = bracket_idxs[code_idx]
            else:
                get_matching_bracket(code, code_idx, bracket_idxs)
                if code[code_idx] == 0:
                    code_idx = bracket_idxs[code_idx]

        elif code[code_idx] == "]" and tape[tape_idx] != 0:
            code_idx = bracket_idxs[code_idx]

        code_idx += 1

    return output


def get_matching_bracket(code, idx, bracket_idxs):
    match_idx = idx + 1

    while match_idx < len(code) and (
        code[match_idx] != "]" or match_idx in bracket_idxs
    ):
        if code[match_idx] == "[" and match_idx not in bracket_idxs:
            get_matching_bracket(code, match_idx, bracket_idxs)
        match_idx += 1

    bracket_idxs[idx] = match_idx
    bracket_idxs[match_idx] = idx


if __name__ == "__main__":
    x = ",>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]"
    print(brain_luck(x, "\n"))
