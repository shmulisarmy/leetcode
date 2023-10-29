#is s a subsecence of t

def solve():
    s = 'abc'
    t = 'aghbclc'
    s_pointer = 0
    for i in t:
        if len(t) - t.index(i) < -1 + len(s):
            return False
        if s[s_pointer] == i:
            s_pointer += 1
        if s_pointer == len(s):
            return True
    print(i)
    return False

print(solve())