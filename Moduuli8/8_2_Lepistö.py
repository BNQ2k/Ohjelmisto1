import mysql.connector
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='pythonUser',
    password='Mansikkakakku',
    autocommit=True
)


def laske_kentat(maakoodi):
    # SQL-kysely
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"

    # kysely
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi.upper(),))
    tulokset = kursori.fetchall()

    # tarkistetaan tuloksia
    if len(tulokset) == 0:
        print(f"Maakoodilla {maakoodi.upper()} ei löytynyt lentokenttiä.")
        return

    # tulokset
    print(f"Lentokenttien määrät maakoodilla {maakoodi.upper()}:")
    for rivi in tulokset:
        tyyppi, maara = rivi
        print(f"{tyyppi}: {maara} kpl")


# Pääohjelma
print("Lentokenttien laskenta")
print("=====================")
koodi = input("Anna maakoodi (esim. FI, US, GB): ")

laske_kentat(koodi)

print("=====================")