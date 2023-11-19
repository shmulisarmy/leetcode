


def do(string = ['a', 'b', 'd', 'a', 'b', 'c', 'b', 'b'], m = 0):
    print(string)
    counter = 0
    dupes = []
    for i in string:
        if i in dupes:
            string = string[string.index(i) + 1:]
            m = max(counter, m)
            break
        counter += 1
        dupes.append(i)
    if string:
        return do() 

print(do())