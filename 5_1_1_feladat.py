"""1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg,
hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót,
és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!"""

colours = ['piros', 'narancs', 'citrom', 'zöld', 'kék', 'lila', 'magenta', 'rózsaszín', 'türkiz', 'fekete', 'fehér', 'szürke']
szin = input("Adj meg egy színt! ")

if szin in colours:
    print(f"A(z) {szin} szín már szerepel a listában.")
else:
    print(f"A(z) {szin} szín nem szerepel a listában.")

print(f"A lista tartalmazza a {colours} színeket.")