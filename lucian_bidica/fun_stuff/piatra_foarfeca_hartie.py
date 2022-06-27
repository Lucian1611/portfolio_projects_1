import random

while True:
    optiuni = ["piatra", "foarfeca", "hartie"]
    computer = random.choice(optiuni)

    player = None

    while player not in optiuni:
        player = input("Alegeti: piatra, foarfeca sau hartie! ").lower()

        if player == computer:
            print("Computer: ", computer)
            print("Egalitate")
        elif player =="piatra" and computer=="hartie":
            print("Computer: ", computer)
            print("Ai pierdut!!!")
        elif player=="piatra" and computer=="foarfeca":
            print("Computer: ", computer)
            print("Ai castigat!!!")
        elif player=="hartie" and computer=="foarfeca":
            print("Computer: ", computer)
            print("Ai pierdut!!!")
        elif player=="hartie" and computer=="piatra":
            print("Computer: ", computer)
            print("Ai castigat!!!")
        elif player=="foarfeca" and computer=="piatra":
            print("Computer: ", computer)
            print("Ai pierdut!!!")
        elif player=="foarfeca" and computer=="hartie":
            print("Computer: ", computer)
            print("Ai castigat!!!")
    play_again=input("Vrei sa mai joci o data? Tasteaza: da sau nu: ").lower()
    if play_again !="da":
        break
print("La revedere!!!")