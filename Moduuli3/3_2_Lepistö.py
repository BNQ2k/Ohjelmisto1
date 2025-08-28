hyttiluokka = input("Kerro hyttiluokkasi (LUX, A, B, C):")
hyttiluokka = hyttiluokka.upper()

if hyttiluokka == "":
    print("Ei hyväksyttävä hyttiluokka.")

elif hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Ei hyväksyttävä hyttiluokka.")