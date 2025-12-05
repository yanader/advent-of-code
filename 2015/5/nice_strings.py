
def niceStrings(fileName):
    niceCount = 0

    with open(fileName, "r") as file:
        for line in file:
            if containsIllegalCombo(line):
                continue
            if containsThreeVowels(line) and containsDoubleLetter(line):
                niceCount+=1

    return niceCount

def niceStringsPartTwo(fileName):
    niceCount = 0
    with open(fileName, "r") as file:
        for line in file:
            if containsLetterSandwich(line) and containsRepeatingPair(line):
                niceCount+=1
    return niceCount

def containsThreeVowels(s):
    vowelCount = 0
    for _ in s:
        if _ in ["a","e","i","o","u"]:
            vowelCount += 1
    return vowelCount >= 3

def containsDoubleLetter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False
        
def containsIllegalCombo(s):
    combos = ["ab","cd","pq","xy"]
    for combo in combos:
        if combo in s:
            return True
    return False

def containsLetterSandwich(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False

def containsRepeatingPair(word):
    for i in range(len(word) - 2):
        if word[i:i+2] in word[i+2:]:
            return True
    return False



fileName = "input.txt"
# testString = "abcdefb"
# print(containsRepeatingPair(testString))
print(niceStringsPartTwo(fileName))


