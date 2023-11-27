
def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    """
    Find all prime numbers within a given range.

    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    list: A list of prime numbers within the given range.
    """
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Example usage:
start = 0
end = 200
print(find_primes(start, end))
#
#In this code, we have two functions: `is_prime` and `find_primes`. 
#
#The `is_prime` function checks if a given number is prime. It does this by iterating through the numbers from 2 to the square root of the given number. If the given number is divisible by any of these numbers, it is not prime and the function returns