import random
def noppaa(tahkot):
    return random.randint(1, tahkot)
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))
heitto = noppaa(tahkojen_maara)
# heittää kunnes tulee suurin silmäluku
while heitto != tahkojen_maara:
    print(f"Heiton silmäluku: {heitto}")
    heitto = noppaa(tahkojen_maara)
else:
    print(f"Heiton silmäluku: {heitto}")
    print("Sait maksimisilmäluvun!")