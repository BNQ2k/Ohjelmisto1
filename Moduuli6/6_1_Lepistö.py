import random
def noppaa():
    return random.randint(1, 6)
heitto = noppaa()
# heittää kunnes tulee kuusi
while heitto != 6:
    print(f"Heiton silmäluku: {heitto}")
    heitto = noppaa()
else:
    print(f"Heiton silmäluku: {heitto}")
