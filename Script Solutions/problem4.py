import __main__
from math import floor
"""
91 x 99 = 9009
nnn x nnn = abccba
Have a loop where we start at 999 x 999 we check if it is 6 digits and a palindrome
if not then we decrease the value of one of the numbers - or just checks all combos and log the highest value   

123321 -> 123 321 -> 123 123

12321 -> 1221 -> do whats above

123454321

"""

def main(digits):
    highest = 0
    a = ''
    b = ''
    for _ in range(digits):
        a += '9'
        b += '9'

    for a_i in range(int(a) + 1, 1, -1):
        for b_i in range(int(b) + 1, 1, -1):
            multiple = str(a_i * b_i)
            if isPalindrome(multiple):
                highest = max(int(multiple), highest)
    return highest

def isPalindrome(num):
    """Wont work for one by one digits"""
    result = None
    if len(num) % 2 == 0:
        halfway = int(len(num)/2)
        # print(halfway)
        head = num[:halfway]
        tail = num[len(num):halfway - 1:-1]
        # print(f'EVEN Head is {head} and Tail is {tail}')
        if head == tail:
            result = True
        else:
            result = False
    else:
        halfway = floor(len(num)/2)
        head = num[:halfway]
        tail = num[len(num):halfway:-1]
        # print(f'ODD Head is {head} and Tail is {tail}')
        if head == tail:
            result = True
        else:
            result = False
    return result

if __main__:
    # print(isPalindrome('903409'))
    print(main(3))