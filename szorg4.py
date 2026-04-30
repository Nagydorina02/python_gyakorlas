szavak = ["Alma", "kÖrte", "fa", "BANAN", "ki", "Szilva"]

kisbetus = list(map(lambda szo: szo.lower(), szavak))

szurt = list(filter(lambda szo: len(szo) >= 3, kisbetus))

print(szurt)