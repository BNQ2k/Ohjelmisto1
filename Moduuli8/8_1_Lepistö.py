import mysql.connector
yhteys = mysql.connector.connect(
    host='localhost' ,
    port=3306 ,
    database='flight_game' ,
    user='pythonUser',
    password='Mansikkakakku' ,
    autocommit = True
)

def ICAO_Kysely(ICAO):

    sql = f"SELECT name FROM airport WHERE ident = '{ICAO}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if kursori.rowcount > 0:
        print(tulos)
    elif kursori.rowcount <= 0:
        print("Ei lentokenttää, jolla kyseinen ICAO-koodi.")
        return

ICAO = input("Anna ICAO-koodi: ")
ICAO_Kysely(ICAO)