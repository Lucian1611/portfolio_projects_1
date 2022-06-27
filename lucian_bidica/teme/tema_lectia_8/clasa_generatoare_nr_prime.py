import time

class NumerePrime:
    def __init__(self, max):
        self.max = max
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif self.numar_prim(self.number):
            return self.number
        else:
            return self.__next__()

    def numar_prim(self, number):
        for divisor in range(2, number - 1):
            if number % divisor == 0:
                return False
        return True

valoare = int(input("Pana la ce valoare sa generam numere prime: "))
numere_prime = NumerePrime(valoare)
# print(primes)
for x in numere_prime:
    print(x)
