# functie care returneaza primul numar neconsecutiv dintr-o lista

def first_non_consecutive(a):
    i = 0
    n = None
    while i < len(a)-1:
        if a[i]+1 != a[i+1]:
            n = a[i+1]
            break
        i += 1
    return n
a= [1,2,3,4,5,10,20,30]
print(first_non_consecutive(a))
