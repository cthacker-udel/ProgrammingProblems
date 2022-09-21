from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


directions = {
    Direction.EAST: [Direction.SOUTH, Direction.NORTH],
    Direction.SOUTH: [Direction.WEST, Direction.EAST],
    Direction.NORTH: [Direction.EAST, Direction.WEST],
    Direction.WEST: [Direction.NORTH, Direction.SOUTH]
}


def execute(code: str) -> str:
    grid = [['*']]
    x = 0
    y = 0
    _dir = Direction.EAST
    pending_command = {}
    ind_ = 0
    max_width = 1
    while ind_ < len(code):
        each_command = code[ind_] if not pending_command else pending_command['cmd']
        if pending_command:
            if pending_command['left'] == 0:
                ind_ = pending_command['end'] if pending_command['end'] != - \
                    1 else len(code) - 1
                pending_command = {}
                continue
            pending_command['left'] -= 1
        if not pending_command and ind_ < len(code) - 1 and code[ind_ + 1].isdigit():
            ## process amt of commands
            command_amt = ''
            ending_digit = -1
            for k in range(ind_ + 1, len(code)):
                if not code[k].isdigit():
                    ending_digit = k
                    break
                command_amt += code[k]
            pending_command = {'cmd': each_command, 'amt': int(
                command_amt), 'left': int(command_amt), 'end': ending_digit}
        elif each_command == 'F':
            if _dir == Direction.SOUTH:
                ## check if we are in bounds
                if len(grid) <= (y + 1):
                    ## add row
                    grid.append([''] * (max_width))
                y += 1
                grid[y][x] = '*'
            elif _dir == Direction.EAST:
                # check if we are in bounds
                if len(grid[y]) <= (x + 1):
                    ## add cell to grid
                    for each_sub_grid in grid:
                        each_sub_grid.append('')
                        max_width = max(max_width, len(each_sub_grid))
                x += 1
                grid[y][x] = '*'
            elif _dir == Direction.NORTH:
                ## check if we are at the end
                if y == 0:
                    # insert new row at the top of the grid
                    grid.insert(0, [''] * (max_width))
                y -= 1 if y != 0 else 0
                grid[y][x] = '*'
            elif _dir == Direction.WEST:
                ## check if we are at the edge
                if x == 0:
                    for each_sub_grid in grid:
                        each_sub_grid.insert(0, '')
                        max_width = max(max_width, len(each_sub_grid))
                x -= 1 if x != 0 else 0
                grid[y][x] = '*'
        elif each_command == 'L':
            _dir = directions[_dir][1]
        elif each_command == 'R':
            _dir = directions[_dir][0]
        ind_ += 1 if not pending_command else 0
    for i in range(len(grid)):
        each_sub_grid = grid[i]
        stringified_sub_grid = ''
        for each_char in each_sub_grid:
            if each_char == '*':
                stringified_sub_grid += "*"
            else:
                stringified_sub_grid += " "
        grid[i] = stringified_sub_grid
    stringified_grid = '\r\n'.join(grid)
    return stringified_grid


if __name__ == '__main__':
    execute("LFFFFFRFFFRFFFRFFFFFFF")
