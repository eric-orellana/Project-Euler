import __main__

def multiplesSum(num):
    multipleList = []
    for i in range(num):
        if i % 3 == 0:
            multipleList.append(i)
        elif i % 5 == 0:
            multipleList.append(i)
    result = 0
    for m in multipleList:
        result += m
    return result

if __main__:
    print(multiplesSum(1000))