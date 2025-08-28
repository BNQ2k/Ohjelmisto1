import random
määrä = int(input("Montako arpakuutionheittoa: "))
lukumäärä = 0
for i in range(määrä):
    heitto = random.randint(1, 6)
    print(f"{i+1}. heitto: {heitto}")
    lukumäärä += heitto

print(f"Silmälukujen summa on {lukumäärä}.")