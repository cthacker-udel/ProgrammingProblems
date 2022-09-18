def find_missing_letter(chars):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if chars[0] in lower_letters:
        starting_ind = lower_letters.index(chars[0])
        for i in range(starting_ind, starting_ind + len(chars)):
            if lower_letters[i] not in chars:
                return lower_letters[i]
    else:
        for i in range(starting_ind, starting_ind + len(chars)):
            if upper_letters[i] not in chars:
                return upper_letters[i]
