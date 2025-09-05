def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def main():
    while True:
        try:
            gallonat = float(input("Anna bensiinin määrä (galloneina, negatiivinen lopettaa):"))
            if gallonat < 0:
                print("Ohjelma lopetetaan.")
                break
            litrat = gallonat_litroiksi(gallonat)
            print(f"{gallonat} gallonaa on {litrat:.3f} litraa.\n" )
        except ValueError:
            print("Virheellinen syöte. Anna luku. \n")
main()