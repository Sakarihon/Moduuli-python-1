import mysql.connector
import geopy.distance

def get_airport_location_by_icao(icao):
    sql = f'SELECT name, latitude_deg, longitude_deg, elevation_ft FROM airport WHERE ident="{icao}"'
    cursor=db_connection.cursor()
    cursor.execute(sql)
    airport_location = cursor.fetchall()
    return airport_location

db_connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Possu2929',
    autocommit=True,
    collation="utf8mb4_general_ci"
)

icao1=input("mikä on 1. icao?")
icao2=input("mikä on 2. icao?")
airport1=get_airport_location_by_icao(icao1)
airport2=get_airport_location_by_icao(icao2)
airport1_coordinates = (airport1[0][1], airport1[0][2])
airport2_coordinates = (airport2[0][1], airport2[0][2])
etäisyys=geopy.distance.distance(airport1_coordinates, airport2_coordinates).km
print(f"etäisyys {airport1[0][0]} - {airport2[0][0]} on {etäisyys:.2f} km")