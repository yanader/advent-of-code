def containsIOL(password):
    if 8 in password: return True
    if 11 in password: return True
    if 14 in password: return True
    return False


def containsTwoDoubles(password):
    i = 0
    while i < len(password) - 3:
        if password[i] == password[i + 1]:
            j = i + 2
            while j < len(password) - 1:
                if password[j] == password[j + 1]:
                    return True
                j += 1
        i += 1
    return False


def containsIncreasingSequence(password):
    i = 0
    while i < len(password) - 2:
        if (password[i] + 1 == password[i + 1]) and (password[i + 1] + 1 == password[i + 2]):
            return True
        i += 1
    return False

def validPassword(password):
    return containsIncreasingSequence(password) and containsTwoDoubles(password) and not(containsIOL(password))

def increment(pw):
    pw[-1] += 1
    i = -1
    while i > -1 * len(pw):
        if pw[i] > 25:
            pw[i] = 0
            pw[i-1] += 1
            if pw[0] == 26:
                pw[0] = 0
        i -= 1
    return pw