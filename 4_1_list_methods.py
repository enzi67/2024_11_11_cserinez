nyelvek = ['Python', 'C', 'C++', 'Java', 'Python']
nyelvek2 = sorted(nyelvek)

# sorbarendezi a listát
nyelvek.sort()
print(nyelvek)

# fordított sorrendbe rendezi a listát
nyelvek.reverse()
print(nyelvek)



# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))
print(nyelvek.index('C++'))

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))
print(nyelvek.count('Py'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)
print('C+++' in nyelvek)


nev = "mama"
print(nev.index("m"))

print(type(nyelvek))
print(type(nev))