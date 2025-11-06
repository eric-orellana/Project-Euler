import __main__

"""
What is the 10,001st prime number
"""

def isPrime(factor):
    return not any(factor % d == 0 for d in range(2, factor))

def main(target):
    primeCount = 1
    n = 3

    while True:
        if isPrime(n):
            # print("n is prime: ", n)
            primeCount += 1
            if primeCount == target:
                return n
        n += 1

if __main__:
    try:
        print("Main returns: ", main(10001))
    except Exception as e:
        print("ERROR: ", e)