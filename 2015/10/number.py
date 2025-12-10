inputNumber = [3,1,1,3,3,2,2,1,1,3]


def countOfMatchingCharacters(n, numberList):
    count = 0
    for _ in numberList:
        if _ == n:
            count += 1
        else:
            return count
    return count

# This is my slow, quadratic implemenation that couldn't work for over 40 iterations
# def calculateNextNumber(inputNumber):
#     i = 0
#     outputNumber = []
#     while i < len(inputNumber):
#         currentNumber = inputNumber[i]
#         currentNumberCount = countOfMatchingCharacters(currentNumber,inputNumber[i:]) 
#         outputNumber.append(currentNumberCount)
#         outputNumber.append(currentNumber)
#         i += currentNumberCount
#     return outputNumber

# This implementation walks the list once in order to reduce time.
def calculateNextNumber(inputNumber):
    output = []
    i = 0
    n = len(inputNumber)
    
    while i < n:
        count = 1
        while i + count < n and inputNumber[i + count] == inputNumber[i]:
            count += 1
        output.append(count)
        output.append(inputNumber[i])
        i += count
    
    return output

for x in range(50):
    print(x)
    # if x < 10:
    #     print(inputNumber)
    inputNumber = calculateNextNumber(inputNumber)

print(len(inputNumber))
# print(inputNumber)