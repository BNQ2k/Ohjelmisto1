pituus = int(input("Kuhan pituus cm:"))
if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuhan pituus on liian pieni, se on vapautettava.")
    print(f"Kuha on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on riittävän pitkä, se voidaan pitää.")