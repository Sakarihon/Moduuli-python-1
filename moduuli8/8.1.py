import mysql.connector

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident="{icao}"'
    cursor=db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

db_connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Possu2929',
    autocommit=True,
    collation="utf8mb4_general_ci"
)

icao=input("mikä on icao?")
airport=get_airport_by_icao(icao)
print(airport)

