import __main__
import math
"""
Find the sum of all the primes below two million.
For under 10 it is 17
"""

def isPrime(factor):
    return not any(factor % d == 0 for d in ([2] + list(range(3, factor, 2))))

def main(limit):
    summedPrimes = 2 # offset for 2 the first prime

    for p in range(3, limit + 1, 2):
        if isPrime(p):
            summedPrimes += p

    return summedPrimes

if __main__:
    try:
        print("Main returns: ", main(200000))
    except Exception as e:
        print("ERROR: ", e)