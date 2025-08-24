sukupuoli = input("Syötä biologinen sukupuoli (mies/nainen): ")
sukupuoli = sukupuoli.lower()

if sukupuoli == "mies":
    mieshemoglobiini = int(input("Syötä miehen hemoglobiiniarvo: "))
    if mieshemoglobiini < 135:
        print("Hemoglobiiniarvo on liian alhainen. Mies voi lahjoittaa verta.")

    elif mieshemoglobiini > 135: