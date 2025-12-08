with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

def countCodeChars(s):
    return len(s)

def countStringChars(s):
    count = 0
    index = 0
    trunc = s[1:-1]
    while index < len(trunc):
        if trunc[index:index + 2] == "\\x":
            print(trunc[index:index + 2])
            count +=1
            index +=4
        elif trunc[index:index + 2] == "\\\"" or trunc[index:index + 2] == "\\\\":
            print(trunc[index:index + 2])
            count +=1
            index +=2
        else:
            print(trunc[index])
            count +=1
            index +=1
    return count

codeChars = 0
stringChars = 0

for item in data:
    codeChars += countCodeChars(item)
    stringChars += countStringChars(item)

print(codeChars)
print(stringChars)       

print(codeChars - stringChars)
        
