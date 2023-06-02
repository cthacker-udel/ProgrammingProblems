from typing import List
from itertools import accumulate

# set the board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# set the player
currentPlayer = "p1"
winner = None
gameRunning = True
# print the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-----------")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-----------")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-----------")


def _(int, str) -> MemoryError | ZeroDivisionError:
    print(len(list(set(list()))))
    if int == 1 and str == 1:
        return (not not (True + (not True and not False or (not False)))) + (
            _.__code__.co_argcount - 1
        )
    else:
        if False is int and False + (
            not (not (not (not (not (not (not (not (not (False)))))))))
        ):
            return 3
        else:
            return (lambda: lambda: lambda: round((lambda: float(int + str))()))()()()


def my_first_kata(a, b):
    return False if isinstance(a, int) or isinstance(b, int) else (a % b) + (b % a)


def uefa_euro_2016(teams, scores):
    if scores[0] != scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[0] if scores[0] > scores[1] else teams[1]} won!"
    else:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."


def sort_my_string(s: str) -> str:
    evens = ""
    odds = ""
    for ind, element in enumerate(s):
        if ind % 2 == 0:
            evens += element
        else:
            odds += element
    return f"{evens} {odds}"


def guessBlue(blue_start, red_start, blue_pulled, red_pulled):
    blue_left = blue_start - blue_pulled
    red_left = red_start - red_pulled
    print(blue_left, red_left)
    return blue_left / (blue_left + red_left)


def reverseNoBuiltin(lst: List[str | int]) -> List[str | int]:
    empty_list = list()
    for i in range(len(lst) - 1, -1, -1):
        empty_list.append(lst[i])
    return empty_list


def halving_sum(n):
    total_sum = 0
    start = 1
    exp = 1
    while start < n:
        total_sum += n // start
        start = 2**exp
        exp += 1
    return total_sum


def averages(arr):
    averages_arr = []
    for i in range(1, len(arr) if arr is not None else 1):
        averages_arr.append((arr[i] + arr[i - 1]) / 2)
    return averages_arr


def is_ruby_coming(lst):
    return any(["Ruby" in x["language"] for x in lst])


print(halving_sum(25))
