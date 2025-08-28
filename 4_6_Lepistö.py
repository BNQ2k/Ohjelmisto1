pisteidenMäärä = int(input("anna pisteiden määrä: "))
import random
kierros = 0
while kierros < pisteidenMäärä:
    print(f"Teemme uuden pisteen")
    #tee uusi piste
    #arvo pisteelle satunnaiset x ja y koordinaatit väliltä 1 -1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Pisteen sijainti on x: {x}, y: {y}")
    paikka =  x**2+y**2
    pointsInCircle = 0

    if paikka < 1 or paikka == 1:
        print(f"Piste on ympyrän sisällä")
        pointsInCircle += 1
    kierros += 1
piEstimate = 4*pointsInCircle/pisteidenMäärä
print(f"Piin liki arvo on {piEstimate}")
    # katsotaan onko piste ympyrän sisällä
