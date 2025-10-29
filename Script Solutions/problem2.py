import __main__

# Generate the fib seq
# Record the even values
# Sum them up - til 4 Million

result = []
LIMIT = 4000000

def evenFibonacci(a, b):
    if (a >= LIMIT or b >= LIMIT):
        return sum(result)
    
    if a % 2 == 0 and a not in result:
        result.append(a)
    if b % 2 == 0 and b not in result:
        result.append(b)

    nextValue = a + b
    return evenFibonacci(b, nextValue)

if __main__:
    print(evenFibonacci(1, 2))