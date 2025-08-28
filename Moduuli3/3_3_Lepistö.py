sukupuoli = input("Syötä biologinen sukupuoli (mies/nainen): ")
sukupuoli = sukupuoli.lower()

# mies
if sukupuoli == "mies":
    mieshemoglobiini = int(input("Syötä miehen hemoglobiiniarvo: "))
    if mieshemoglobiini < 134:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif mieshemoglobiini <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on liian korkea.")

# nainen
if sukupuoli == "nainen":
    naishemoglobiini = int(input("Syötä naisen hemoglobiiniarvo: "))
    if naishemoglobiini < 117:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif naishemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on liian korkea.")