"""2.2 Feladat
Alakítsd át úgy az előző porgramot, hogy az ne csak kis, hanem a nagy "A" betűvel kezdődő
szavakat is elfogadja."""

def feladat():

    szavak = []

    print("Szervusz! Adj meg olyan szavakat, amelyek 'a' betűvel kezdődnek!")
    print("A nem 'a' betűvel kezdődő szavakat a rendszer nem fogja tárolni.")
    print("Ha kész vagy, nyomj ENTER-t a program befejezéséhez!")

    while True:
        szo = input("Adj meg egy szót: ")

        if szo == "":
            break
        
        if szo.lower().startswith('a'):
            szavak.append(szo)
        else:
            print(f"A '{szo}' nem 'a' betűvel kezdődik, adjon meg egy újabb szót!")

    print("A tárolt szavak:")
    for szo in szavak:
        print(szo)

feladat()