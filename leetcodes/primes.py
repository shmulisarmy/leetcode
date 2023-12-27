import sys

def get_primes(final_number):
    """Returns a list of prime numbers until and including 'num'."""

    lst = list(range(2, final_number + 1))

    for num in lst:
        i = num
        while i <= final_number:
            i += num
            if i in lst:
                lst.remove(i)

    return lst

num = 100
if len(sys.argv) > 1:
    num = int(sys.argv[1])

print(get_primes(num))