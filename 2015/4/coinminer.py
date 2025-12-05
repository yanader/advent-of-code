import hashlib

notFound = True
coin = 0

while(notFound):
    h = hashlib.md5()
    h.update(b"iwrupvqb" + str(coin).encode())
    
    if h.hexdigest()[0:6] == "000000":
        notFound = False
    else:
        coin += 1


print(coin)
print(h.hexdigest())

