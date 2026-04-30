import random

def napi_idezet():
    idezetek = [
        "A tudás hatalom.",
        "Soha ne add fel.",
        "Gyakorlás teszi a mestert.",
        "Légy kitartó.",
        "Higgy magadban."
    ]
    while True:
        yield random.choice(idezetek)

gen = napi_idezet()

print(next(gen))
print(next(gen))

for _ in range(5):
    print(next(gen))