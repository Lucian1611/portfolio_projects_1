import itertools
import string
import time

toate_caracterele = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
lungime_parola = int(input("Cate caractere doriti sa aiba parola? "))


def generator_parola(lungime_parola):
    for x in toate_caracterele:
        for coada in itertools.product(toate_caracterele, repeat=lungime_parola - 1):
            yield x + ''.join(coada)
    yield itertools.product(toate_caracterele, repeat=lungime_parola)


parole = generator_parola(lungime_parola)
parola = iter(parole)

contor = 0
t = time.process_time()
while True:
    try:
        print(next(parola))
        contor += 1
    except StopIteration:
        break
print("Pentru configuratia specificata s-au gasit " ,contor, " combinatii")
elapsed_time = time.process_time() - t
print("Processing time: " , elapsed_time, " secunde")