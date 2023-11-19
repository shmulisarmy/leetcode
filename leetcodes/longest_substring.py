


def do(string = ['a', 'b', 'd', 'a', 'b', 'c', 'b', 'b'], m = 0):
    counter = 0
    dupes = []
    for i in string:
        if i in dupes:
            string = string[string.index(i) + 1:]
            if counter > m:
                m = counter
            break
        counter += 1
        dupes.append(i)
    if string:
        return do() 

print(do())