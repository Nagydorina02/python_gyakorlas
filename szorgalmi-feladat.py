"""
Ötödik
szorgalmi
feladat.
"""
def feldolgozas(kerdes):
    if kerdes.endswith("?"):
        print("Ez bizony egy kérdés")

    if not any(karakter.isdigit() for karakter in kerdes):
        print("Ebben egy számjegy sem volt.")

    pontok = kerdes.count(".")
    print("A kérdés", pontok, "darab pontot tartalmazott.")

    return "Feldolgozva"

while True:
    kerdes = input("Kerdes: ")

    if kerdes == "exit" or kerdes == "quit":
        print("Bye!")
        break

    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Válasz: " + str(valasz))

print("VEGE.")