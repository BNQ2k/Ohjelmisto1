import math
m = math
def pizza(halkaisija, eurot):
    pinta_ala = (m.pi / 4) * (halkaisija/2)** 2 (halkaisija / (10000))
    return eurot / pinta_ala

pizza1_hinta = float(input("MIkä on pizzan hinta?"))
pizza1_halkaisija = float(input("Mikä on pizzan halkaisija?"))
pizza2_hinta = float(input("Mikä on pizzan hinta?"))
pizza2_halkaisija = float(input("Mikä on pizzan halkaisija?"))

pizza1_neliohinta = pizza (pizza1_halkaisija, pizza1_hinta)
pizza2_neliohinta = pizza (pizza2_halkaisija, pizza2_hinta)

if pizza1_neliohinta < pizza2_neliohinta:
    print("Pitsa 1 on parempi.")
elif pizza2_neliohinta < pizza1_neliohinta:
    print("Pitsa 2 on parempi.")
else:
    print("Pizzat ovat yhtä hyviä.")