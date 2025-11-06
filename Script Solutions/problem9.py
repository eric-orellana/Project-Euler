import __main__
import math
"""
a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000
Find the product abc

iterate through different values of a 
    then add one to b and iterate up to say 100
        check if root of c^2 is a natural number
            if yes then we will check that a + b + c = 1000
                if yes we got this answer 
                otherwise continue the loop within b
"""
LIMIT = 1000

def main():
    for a in range(1, LIMIT - 1):
        for b in range(2, LIMIT):
            c_sqrd = a**2 + b**2
            c = math.isqrt(c_sqrd)

            if (c * c == c_sqrd):
                print(f"triplet found {a}, {b}, {c}")

                if (a + b + c == 1000):
                    print(f"ANSWER: a is {a} b is {b} and c is {c}")
                    return a * b * c

    return "Nothing was found"

if __main__:
    try:
        print("Main returns: ", main())
    except Exception as e:
        print("ERROR: ", e)