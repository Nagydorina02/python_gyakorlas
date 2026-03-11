"""
Negyedik
szorgalmi
feladat.
"""

x = 7
y = 4
if y > 5:
    print("Y nagyobb, mint 2.")
    if y % 2 == 0:
        print("y nagyobb, mint 5.")
else:
    print("Y kisebb vagy egyenlő, mint 2.")

for nev in ["Dóri", "Csenge", "Bia"]:
    print(nev)
    if nev == "Bia":
        print("Szia Bia!")

while y < 8:
    print("y még kisebb, mint 8.")
    y += 1
    print("y értéke: " + str(y))

def fuggveny():
    print("Fut!")

    return "megáll"

fuggveny()
fuggveny()
fuggveny()
fuggveny()
fuggveny()
eredmeny = fuggveny()
print("És " + eredmeny + "t.")
