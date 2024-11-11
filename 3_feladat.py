"""3. Feladat
A program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel
oszthatóakat rögzítse egy listában. A végén jelenítse meg a listát a képernyőn, és írja ki
azt is, hány elemből áll a lista."""

def feladat():

    import random

    oszthato_4_gyel = []

    for _ in range(10):
        veletlen_szam = random.randint(0, 50)
        if veletlen_szam % 4 == 0:
            oszthato_4_gyel.append(veletlen_szam)

    print("A 4-gyel osztható számok:", oszthato_4_gyel)
    print("A lista hossza:", len(oszthato_4_gyel))

feladat()