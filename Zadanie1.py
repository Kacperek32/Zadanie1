def palindrom(o):
    n = len(o)
    for i in range (n-1):
        if o[i] != o[n-1-i]:
            return False
        return True
print("Daj słowo")
word = input() 
print("Dane słowo" + (" jest" if(palindrom(word)) else " nie jest") + " palindromem")

