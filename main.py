from hmac import new
from os import times_result

print("hello")
#ez egy komment
"""
több
soros
komment
"""
x = 10
print(x)
x = 30
print(x)
y = 1.5456
print(y)
nev :str = "Bumbus"
print(nev)

print([1, 2, 3, 4, 5])

print("hali" + " gali")
print("hello" + str(12))
print(f"hello {12} {nev}")
tuple_szamok = (2,4)
print(f"szamok {(1,2,5,7)}, tuple_szamok: {tuple_szamok}")
print(range(5))
lista = [1,1,1,1,1,3,4]
print(lista)
halmaz ={1,1,1,1,1,3,4}
print(halmaz)
szotar = {"név": "Anna", "kor": 20}
print(szotar)

logikai = True
print(logikai)

ertek = None
print(ertek)

szam1 = 11

nev ="Jani"
Nev ="Jancsi"
print(nev + " es " + Nev + " barátok")
PI = 3.14
print(PI)

print(2 + 2 * 3 - 4 /2 + 0.5)
x = 5
y = 2
print("x mod y:" +str(x%y))

print("Három az értéke y-nak? " + str(y == 3))
print("Nem három az értéke y-nak? " + str(y != 3))
print("Y kisebb, mint 3? " + str(y < 3))
print("Y kisebb, mint 3? " + str(y > 3))
print("Y kisebb, mint 3? " + str(y <= 3))
print("Y kisebb, mint 3? " + str(y >= 3))

print("Y kisebb, mint 3? " + str(y < 3 or y == 3))


if y > 5:
    print("y nagyobb, mint 5")
    if y % 2 == 0:
        print("y nagyobb, mint 5")
else:
    print("y kisebb vagy egyenlő, mint 5")


for i in range(5):
        print(i)

for nev in ["Anna", "Jani", "Jancsi"]:
    print(nev)
    if nev == "Anna":
        print("Szia Anna")


print("VÉGE")

while y < 10:
    print("y még kisebb, mint 10")
    y += 1
    print("y értéke: " + str(y))

def fuggveny():
    print("Ez egy függvény")

    return "Alma"

print("következő sor")
fuggveny()
fuggveny()
fuggveny()
eredmeny = fuggveny()
print("A függvény vissza adott egy " + eredmeny + "-t")


def osszead(a,b):
    osszeg = a+b
    return osszeg

print("Összeg " + str(osszead(3,4)))