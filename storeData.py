import mysql.connector

# Set up the connection parameters
config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'cpe314_database',
  'port': '3306',
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# push data into database
def pushData(node, time, humidity, temp, thermal):
    stmt = "INSERT INTO `data` (`Node`, `Time`, `Humidity`, `Temperature`, `ThermalArray`) VALUES (%s, %s, %s, %s, %s)"
    values = (node, time, humidity, temp, thermal)
    cursor.execute(stmt, values)
    cnx.commit()