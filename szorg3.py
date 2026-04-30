szamok = [-5, 3, 10, -2, 7, 0, 8]

gen = (szam * 10 for szam in szamok if szam > 0)

for ertek in gen:
    print(ertek)