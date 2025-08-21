kertoja = float(input("Kuinka monena päivänä viikossa syöt opiskelijaravintolassa:"))
hinta = float(input("Kuinka paljon opiskelijalounas maksaa:"))
ruokaostokset = float(input("Kuinka paljon käytät ruokaostoksiin viikossa: "))


viikossa = (hinta * kertoja) + ruokaostokset
päivässä = viikossa / 7

print("Ruokaan käytetty raha keskimäärin: ")
print()

print("Yhdessä päivässä: ", päivässä, "euroa")
print("Viikossa: ", viikossa, "euroa")
