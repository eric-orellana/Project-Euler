import __main__

def greatestPrimeFactor(num):
    quotient = num
    for factor in range(3, quotient):
        if any(factor % d == 0 for d in range(2, factor)):
            continue
        
        if quotient % factor == 0:
            quotient = int(quotient / factor)
            if any(quotient % d == 0 for d in range(2, quotient)):
                continue
            else:
                return quotient
    return

if __main__:
    print(greatestPrimeFactor(600851475143))