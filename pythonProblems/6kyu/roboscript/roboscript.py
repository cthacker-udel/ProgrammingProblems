
from pprint import pprint


colors = {
    "F": "pink",
    "L": "red",
    "R": "green",
    "digit": "orange"
}

ending_span = "</span>"


def generate_starting_span(color):
    return '<span style="color: {}">'.format(color)


def highlight(code: str) -> str:
    code = list(code)
    start_highlight = -1
    digits = "0123456789"
    highlighting_chars = 'FLR{}'.format(digits)
    non_highlighting_chars = '()'
    current_char = ''
    old_char = ''
    index = 0
    while index < len(code):  # O(n)
        current_char = code[index]
        start_highlight = index if not old_char else start_highlight
        old_char = current_char if not old_char else old_char
        if current_char in non_highlighting_chars:
            if old_char in highlighting_chars:
                code.insert(index, ending_span)
                code.insert(start_highlight,
                            generate_starting_span(colors["digit" if old_char in digits else old_char]))
            old_char = ''
        elif start_highlight != -1 and current_char != old_char and old_char in highlighting_chars and (current_char in highlighting_chars or current_char in non_highlighting_chars):
            if current_char in digits and old_char in digits:
                index += 1
                continue
            code.insert(index, ending_span)
            code.insert(start_highlight,
                        generate_starting_span(colors["digit" if old_char in digits else old_char]))
            old_char = current_char
            start_highlight = index + 2 if current_char in highlighting_chars else index + 3
        index += 1
    code.insert(index, ending_span)
    code.insert(start_highlight,
                generate_starting_span(colors["digit" if old_char in digits else old_char]))
    return ''.join(code)


if __name__ == '__main__':
    highlight("FFFR(345F2LL")


# <span style="color: pink">FFF</span>
# <span style="color: green">R</span>
# <span style="color: orange">3</span>
# <span style="color: orange">4</span>
# <span style="color: orange">5</span>
# <span style="color: pink">F</span>
# <span style="color: orange">2</span>
# <span style="color: red">LL</span>

# ' should equal '

# <span style="color: pink">FFF</span>
# <span style="color: green">R</span>
# <span style="color: orange">345</span>
# <span style="color: pink">F</span>
# <span style="color: orange">2</span>
# <span style="color: red">LL</span>'
