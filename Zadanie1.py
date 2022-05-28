def palindrom(o):
    n = len(o)
    for i in range (n-1):
        if o[i] != o[n-1-i]:
            return False
        return True