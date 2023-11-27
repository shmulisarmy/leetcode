


def do(string = ['a', 'b', 'd', 'a', 'b', 'c'], m = 0):
    print(string)
    counter = 0
    dupes = []
    for i in string:
        if i in dupes:
            print(string.index(i))
            string = string[string.index(i)+1:]
            m = max(counter, m)
            counter += 1
            dupes.append(i)
            break
        
    if string:
        return do() 

print(do())