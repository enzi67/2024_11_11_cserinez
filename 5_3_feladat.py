"""3. Feladat
Írj egy programot, amely a felhasználótól betűket kér be mindaddig, amíg az nem ad meg betűt, csupán egy ENTER-t üt!

A program vizsgálja meg a megadott betűt, és tárolja el egy listában, ha az még nem szerepel benne (a felhasználó korábban még nem adta meg)!
A program NE különböztesse meg a kis- és nagybetűket egymástól, de olyan formában tárolja el a betűket mindig, ahogy a felhasználó megadta.

Ha a megadott betű már szerepel a listában írja ki, a képernyőre, hogy "Ezt a betűt már rögzítettem."!

Minden egyes adatbekérés után írja ki a már rögzített betűket ábécé sorrendben (elöl a nagybetűk, utána a kisbetűk ábécé sorrendben)!
"""

betuk = []

while True:
    input_betu = input("Adj meg egy betűt (ENTER a kilépéshez): ")

    if input_betu == "":
        break

    if len(input_betu) == 1 and input_betu.isalpha():
        kis_nagy_betu = input_betu.lower()

        if kis_nagy_betu not in [betu.lower() for betu in betuk]:
            betuk.append(input_betu)
            betuk_sorted = sorted(betuk, key=lambda x: (x.lower(), x))
            print("Rögzített betűk sorrendben:", ", ".join(betuk_sorted))
        else:
            print("Ezt a betűt már írtad.")
    else:
        print("Kérlelk, csak egy betűt adj meg!")

print("A véglegesen rögzített betűk:", ", ".join(betuk))
