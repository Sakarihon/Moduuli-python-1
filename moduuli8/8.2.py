import mysql.connector

def get_airport_counts_by_type(db_connection, iso_country):
    sql = f'SELECT COUNT(*), type FROM airport WHERE iso_country=%s GROUP BY type'
    cursor=db_connection.cursor()
    cursor.execute(sql, (iso_country,))
    airport_counts = cursor.fetchall()
    cursor.close()
    return airport_counts

db_connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Possu2929',
    autocommit=True,
    collation="utf8mb4_general_ci"
)

iso_country=input("mikä on maakoodi?")
airport_counts=get_airport_counts_by_type(db_connection, iso_country)

if airport_counts:
    print(f"Lentokenttien lukumäärä tyypeittäin maassa {iso_country}:")
    for count, airport_type in airport_counts:
        if airport_type == 'small_airport':
            print(f"Pieniä lentokenttiä {count} ")
        elif airport_type == 'heliport':
            print(f"Helikopterikenttiä {count} ")
        elif airport_type == 'medium_airport':
            print(f"Keskikokoisia lentokenttiä {count} ")
        elif airport_type == 'large_airport':
            print(f"Suuria lentokenttiä {count} ")
        else:
            print(f"{airport_type} {count} ")
else:
    print(f"Maassa {iso_country} ei ole lentokenttiä.")


db_connection.close()