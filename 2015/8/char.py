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
            count +=1
            index +=4
        elif trunc[index:index + 2] == "\\\"" or trunc[index:index + 2] == "\\\\":
            count +=1
            index +=2
        else:
            count +=1
            index +=1
    return count

def countEncodeChars(s):
    count = 0
    for _ in s:
        if _ == "\"" or _ == "\\":
            count += 2
        else:
            count += 1
    return count + 2



encodeChars = 0
codeChars = 0
stringChars = 0

for item in data:
    codeChars += countCodeChars(item)
    stringChars += countStringChars(item)
    encodeChars += countEncodeChars(item)

print(encodeChars)
print(stringChars)       

print(encodeChars - codeChars)
        
# test = data[1]
# print(countEncodeChars(test))