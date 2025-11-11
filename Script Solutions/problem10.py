import __main__
import math
"""
Find the sum of all the primes below two million.
For under 10 it is 17
"""

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    r = int(math.isqrt(n))
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True

def main(limit):
    summedPrimes = 2 # offset for 2 the first prime

    for p in range(3, limit + 1, 2):
        if is_prime(p):
            summedPrimes += p

    return summedPrimes

if __main__:
    try:
        print("Main returns: ", main(2000000))
    except Exception as e:
        print("ERROR: ", e)