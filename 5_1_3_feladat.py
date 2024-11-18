"""1.3 Feladat
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által megadott szín kerüljön felvételre a listába,
és csak ezután történjen meg a lista tartalmának kiírása!"""

colours = ['piros', 'narancs', 'citrom', 'zöld', 'kék', 'lila', 'magenta', 'rózsaszín', 'türkiz', 'fekete', 'fehér', 'szürke']
szin = input("Adj meg egy színt! ")

if szin in colours:
    print(f"A(z) {szin} {colours.count(szin)} -szer szerepel a listában.")
else:
    print(f"A(z) {szin} szín nem szerepel a listában.")

    kiegeszites = [(szin)]
    colours.extend(kiegeszites)

print(f"A lista tartalmazza a {colours} színeket.")