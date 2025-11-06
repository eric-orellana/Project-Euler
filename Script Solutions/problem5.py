import __main__

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""
TWENTYLIST = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def main(numRange):
    multiple = numRange
    successFlag = False

    while (not successFlag):
        # print(f"Multiple is {multiple}")

        for n in TWENTYLIST:
            if multiple % n != 0:
                multiple += 1
                break
            else:
                if n == 20:
                    successFlag = True
    return multiple

if __main__:
    try:
        print("Main returns: ", main(20))
    except Exception as e:
        print("ERROR: ", e)