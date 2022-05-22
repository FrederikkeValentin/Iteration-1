from Database_Connection_MySQL import *

forbindelse = MySQL_connector()
connection = forbindelse.opret_forbindelse_til_databasen()
connection.get_alt_information()