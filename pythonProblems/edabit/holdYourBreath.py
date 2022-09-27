def diving_minigame(intervals):
    allowed_extra = 10
    curr_breath = 10
    for eachinterval in intervals:
        if curr_breath == 0:
            return False
        elif eachinterval >= 0 and curr_breath < 10:
            if allowed_extra > 0:
                extra_off = abs(curr_breath - 10)
                curr_breath += extra_off if extra_off <= 4 else 4
                allowed_extra -= extra_off if extra_off <= 4 else 4
        elif eachinterval < 0:
            curr_breath -= 2
    return curr_breath != 0


if __name__ == '__main__':
    diving_minigame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # True)
    diving_minigame([-5, -15, -4, 0, 5])  # True)
    diving_minigame([0, -4, 0, -4, -5, -2])  # True)
    diving_minigame([-4, -3, -4, -3, 5, 2, -5, -20, -42, -4, 5, 3, 5])  # True)

    diving_minigame([-3, -6, -2, -6, -2])  # False)
    diving_minigame([-4, -5, -2, -7, 2, -1000, -2000, -1])  # False)
    diving_minigame([1, 2, 1, 2, 1, 2, 1, 2, 1, -3, -4, -5, -3, -4])  # False)
    diving_minigame([-5, -5, -5, -5, -5, 2, 2, 2, 2, 2, 2, 2, 2])  # False)
