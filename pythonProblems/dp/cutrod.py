import random


def memo_cut_rod_aux(p, n, r):
    q = -1
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memo_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def memo_cut_rod(p, n):
    r = [0] * (n + 1)
    for i in range(n + 1):
        r[i] = -1
    return memo_cut_rod_aux(p, n, r)


if __name__ == '__main__':
    range_ = 20
    prices = {}
    for i in range(1, range_ + 1):
        prices[i] = random.randint(10, 200)
    print(memo_cut_rod(prices, range_))
