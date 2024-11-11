"""1.2 Feladat
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a
felhasználót, hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket,
és lépjen ki.
"""
nevek = []

def a():

    folytat = True
    while folytat:
        if len(nevek) >= 2:
            folytat = False
        nev = input("Adj meg egy keresztnevet! ")
        nevek.append(nev)
    print("Nincs lehetőség újabb bevitelre.")
    print(nevek)


def b():


a()
b()        