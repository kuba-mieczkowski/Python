# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
random.seed(9876)
FLOORS = 10
UP = 6
DOWN = 2


def rzucaj(l):
    rzuty = [None for i in range(l)]
    poprzedni_rzut = None
    i = 0
    while i < len(rzuty):
        rzut = random.randint(1, 100)
        if rzut <= 50 and poprzedni_rzut == "R":
            poprzedni_rzut = None
            continue
        if rzut <= 50:
            wynik = "R"
            poprzedni_rzut = "R"
        else:
            wynik = "O"
            poprzedni_rzut = "O"
        rzuty[i] = wynik
        i += 1
    return rzuty


def sprawdz(rzuty, stopnie_na_pietro):
    pozycja = 0
    for i in range(len(rzuty)):
        if rzuty[i] == "R":
            pozycja += UP
        else:
            pozycja -= DOWN
    pietro = pozycja // stopnie_na_pietro
    print(pozycja, stopnie_na_pietro)
    return pozycja, pietro


def main(stopnie_na_pietro=10):
    # wylosuj 10-elementowa liste L
    L = [random.randrange(51, 100, 2) for i in range(10)]
    print(f"Rzuty w próbach: {L}")
    pozycja = [0 for i in range(10)]
    sukces = [None for i in range(10)]
    for i in range(len(L)):
        rzuty = rzucaj(L[i])
        print(f"Próba numer {i + 1}.")
        print(f"Rzuty: {rzuty}")
        stopnie, pietro = sprawdz(rzuty, stopnie_na_pietro)
        pozycja[i] = stopnie
        sukces[i] = pietro >= 10
        print(f"Udało się dojść na {stopnie} stopień, czyli na {pietro} piętro.")
        print()
    print(f"Stopnie osiągnięte we wszystkich próbach: {pozycja}")
    print(f"Sukces/porażka każdej z prób: {sukces}")





if __name__ == '__main__':
    main()


