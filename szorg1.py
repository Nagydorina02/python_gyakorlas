szavak = ["alma", "korte", "banan", "eper", "szilva", "barack"]

uj_lista = [szo.upper() for szo in szavak if len(szo) <= 5]

print(uj_lista)