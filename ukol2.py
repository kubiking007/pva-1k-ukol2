import random

moznosti = ["kámen", "nůžky", "papír"]
vyhrava_nad = {"kámen": "nůžky", "nůžky": "papír", "papír": "kámen"}
porazi_ho = {"kámen": "papír", "nůžky": "kámen", "papír": "nůžky"}

vyhry = 0
prohry = 0
remizy = 0

while True:
    obtiznost = input("Zvolte ontížnost (1 - snadné, 2 - střední, 3 - těžké): ").strip()
    if obtiznost not in ["1", "2", "3"]:
        print("Neplatná volba obtížnosti, zkus to znovu.")
        continue
    break

while True:
    volba = input("Zadejte kámen, nůžky, papír (nebo 'konec')").lower().strip()

    if volba == "konec":
        break

    if volba not in moznosti:
        print("Neplatná volba, zkus to znovu.")
        continue

    if obtiznost == "1":
        pocitac = vyhrava_nad[volba]
    elif obtiznost == "2":
        pocitac = random.choice(moznosti)
    else:
        pocitac = porazi_ho[volba]

    print(f"Počítač zvolil: {pocitac}")
    
    if volba == pocitac:
        print("Remíza!")
        remizy += 1
    elif vyhrava_nad[volba] == pocitac:
        print("Vyhrál jsi!")
        vyhry += 1
    else:
        print("Prohrál jsi!")
        prohry += 1

print("\n--- Konečné skóre ---")
print(f"Výhry: {vyhry}")
print(f"Prohry: {prohry}")
print(f"Remízy: {remizy}")
