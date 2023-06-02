from typing import Dict, List


def simple_assembler(commands: List[str]) -> Dict[str, int]:
    """
    Takes in a program string, and returns the registers present within the program

    Args:
        commands (List[str]): Array of commands to execute

    Returns:
        Dict[str, str]: The registers from executing the program
    """
    registers = {}
    command_ind = 0
    while command_ind < len(commands):
        split_command = commands[command_ind].split(" ")
        command = split_command[0]
        if command == "inc" or command == "dec":
            register = split_command[1]
            if register in registers:
                registers[register] += 1 if command == "inc" else -1
            command_ind += 1
        elif command == "mov":
            register = split_command[1]
            value: str = split_command[2]
            if value.replace("-", "").isnumeric():
                registers[register] = int(value)
            elif value in registers:
                registers[register] = registers[value]
            command_ind += 1
        else:
            # jump
            check_register = split_command[1]
            if (
                not check_register.replace("-", "").isnumeric()
                and registers[check_register] != 0
            ):
                ## execute jump
                command_ind += int(split_command[2])
            elif (
                check_register.replace("-", "").isnumeric() and int(check_register) != 0
            ):
                command_ind += int(split_command[2])
            else:
                command_ind += 1
    return registers


if __name__ == "__main__":
    code = """\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a"""
    print(simple_assembler(code.splitlines()), {"a": 1})

    code = """\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a"""
    print(simple_assembler(code.splitlines()), {"a": 409600, "c": 409600, "b": 409600})
    print(simple_assembler(["mov a -10", "mov b a", "inc a", "dec b", "jnz a -2"]))
