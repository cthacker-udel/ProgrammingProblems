def x(n):
    if n < 3 or n % 2 == 0:
        return ''
    else:
        drawing = []
        line_ = ''
        left_ = 0
        right_ = n - 1
        for _ in range(n):
            for j in range(n):
                if j == left_ or j == right_:
                    line_ += '■'
                else:
                    line_ += '□'
            drawing.append(line_)
            line_ = ''
            left_ += 1
            right_ -= 1
        return '\n'.join(drawing)


if __name__ == '__main__':
    x(5)
