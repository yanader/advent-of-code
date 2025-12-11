from helpers import *

# password = [7,23,1,23,22,23,1,0]
password = [7,23,1,23,23,24,25,25]



while True:
    password = increment(password)
    if validPassword(password):
        break


print(password)

for _ in password:
    print(chr(65+_), end=" ")