import sys

caching = {}

def break_path_into_smaller_path(m, n):
    if m == 1 or n == 1:
        return 1
    
    if (m, n-1) in caching:
        potential_path1 = caching[(m, n-1)]
    elif (n-1, m) in caching:
        potential_path1 = caching[(n-1, m)]
    else:
        potential_path1 = break_path_into_smaller_path(m, n - 1)
        caching[(m, n-1)] = potential_path1

    if (m-1, n) in caching:
        potential_path2 = caching[(m-1, n)]
    elif (n, m-1) in caching:
        potential_path2 = caching[(n, m-1)]
    else:
        potential_path2 = break_path_into_smaller_path(m-1, n)
        caching[(m-1, n)] = potential_path2

    return potential_path1 + potential_path2


if len(sys.argv) == 3:
    print(break_path_into_smaller_path(int(sys.argv[1]), int(sys.argv[2])))