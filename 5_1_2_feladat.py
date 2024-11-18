"""1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által
megadott szín a listában! Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""

colours = ['piros', 'narancs', 'citrom', 'zöld', 'kék', 'lila', 'magenta', 'rózsaszín', 'türkiz', 'fekete', 'fehér', 'szürke']
szin = input("Adj meg egy színt! ")

if szin in colours:
    print(f"A(z) {szin} {colours.count(szin)} -szer szerepel a listában.")
else:
    print(f"A(z) {szin} szín nem szerepel a listában.")

print(f"A lista tartalmazza a {colours} színeket.")