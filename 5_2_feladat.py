"""2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását
a listából, majd írja ki a módosított listát a képernyőre!"""

import random

szamok = [random.randint(1, 3) for _ in range(10)]

print("A generált számok listája:", szamok)
1
while True:
    try:
        keresett_szam = int(input("Kérem adjon meg egy számot [1;3]: "))
        if keresett_szam not in [1, 2, 3]:
            print("Kérem, hogy a szám [1;3] intervallumból legyen!")
        else:
            break
    except ValueError:
        print("Kérem érvényes számot adjon meg!")

szamok = [szam for szam in szamok if szam != keresett_szam]

print("A módosított lista:", szamok)
