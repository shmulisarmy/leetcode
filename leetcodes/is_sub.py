#is s a subsecence of t

def solve():
    s = 'abc'
    t = 'aghbclc'
    s_pointer = 0
    for i in t:
        if len(t) - t.index(i) < -1 + len(s):
            return False
        if s[s_pointer] == i:
            sp += 1
        if sp == len(s):
            return True
    print(i)
    return False

print(solve())