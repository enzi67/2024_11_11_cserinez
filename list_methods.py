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

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)
print('C+++' in nyelvek)
  