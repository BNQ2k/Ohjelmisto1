import mysql.connector
from geopy.distance import geodesic

# Yhdistetään tietokantaan
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='pythonUser',
    password='Mansikkakakku',
    autocommit=True
)


def hae_koordinaatit(icao_koodi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_koodi.upper(),))
    tulos = kursori.fetchone()

    if tulos is None:
        print(f"Lentokenttää ICAO-koodilla {icao_koodi.upper()} ei löytynyt.")
        return None

    latitude, longitude = tulos
    return (latitude, longitude)


def laske_etaisyys(icao1, icao2):
    koordinaatit1 = hae_koordinaatit(icao1)
    koordinaatit2 = hae_koordinaatit(icao2)

    if koordinaatit1 is None or koordinaatit2 is None:
        return None

    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers
    return etaisyys


# Pääohjelma
print("Lentokenttien välinen etäisyys")
print("==============================")

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

etaisyys = laske_etaisyys(icao1, icao2)

if etaisyys is not None:
    print(f"Lentokenttien {icao1.upper()} ja {icao2.upper()} välinen etäisyys on {etaisyys:.2f} km.")
else:
    print("Etäisyyttä ei voitu laskea. Tarkista ICAO-koodit.")

print("==============================")