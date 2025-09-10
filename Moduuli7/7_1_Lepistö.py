vuodenajat = ["kevät", "kesä", "syksy", "talvi"]
kuukausi = int(input("Syötä kuukausi 1-12:"))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print(f"Kuukausi {kuukausi} on vuodenajan {vuodenajat[3]} kuukausi.")

elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print(f"Kuukausi {kuukausi} on vuodenajan {vuodenajat[0]} kuukausi.")

elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print(f"Kuukausi {kuukausi} on vuodenajan {vuodenajat[1]} kuukausi.")

elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print(f"Kuukausi {kuukausi} on vuodenajan {vuodenajat[2]} kuukausi.")