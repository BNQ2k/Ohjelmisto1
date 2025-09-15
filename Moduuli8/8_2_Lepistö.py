import mysql.connector
yhteys = mysql.connector.connect(
    host='localhost' ,
    port=3306 ,
    database='flight_game' ,
    user='pythonUser',
    password='Mansikkakakku' ,
    autocommit = True
)

