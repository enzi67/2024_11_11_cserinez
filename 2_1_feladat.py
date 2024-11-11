szavak = []

while True:
    szo = input("Adj meg egy szót: ")  #.strip()
    
    if szo == "":
        break
    
    if szo.lower().startswith('a'):
        szavak.append(szo)
    else:
        print(f"A '{szo}' nem 'a' betűvel kezdődik, figyelmen kívül hagyjuk.")

print("\nA tárolt szavak:")
for szo in szavak:
    print(szo)
