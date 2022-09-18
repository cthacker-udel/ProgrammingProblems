def add(a): return a(lambda b: a + b)
def mul(a): return a(lambda b: a * b)
def pow(a): return a(lambda b: a**b)


"""
test.assert_equals(unchurch( add (one) (two) ), 3)
test.assert_equals(unchurch( add (two) (four) ), 6)
test.assert_equals(unchurch( add (zero) (three) ), 3)
test.assert_equals(unchurch( add (zero) (zero) ), 0)

"""
