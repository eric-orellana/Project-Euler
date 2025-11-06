import __main__

"""
1^2 + 2^2 + ... 10^2 = 385
(1 + 2 + ... 10)^2 = 3025
3025 - 385 = 2640
Do it for up to 100
"""

def main(numRange):
    sumofSquare = 0
    squareofSum = 0

    for n in range(1, numRange + 1):
        sumofSquare += n**2
        squareofSum += n
    squareofSum = squareofSum**2

    high = max(sumofSquare, squareofSum)
    lower = min(sumofSquare, squareofSum)

    return high - lower

if __main__:
    try:
        print("Main returns: ", main(100))
    except Exception as e:
        print("ERROR: ", e)