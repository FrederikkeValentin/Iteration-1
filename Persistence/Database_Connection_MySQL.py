import mysql.connector
from mysql.connector import errorcode

class MySQL_connector:
    """Dette er en class for connecter fra MySQL til Python med 2 attributter"""
    # Connect er en constructor, der opretter forbindelse til vores database og retunerer et objekt
    my_db = my_cursor = None

    def __init__(self):
        global min_database, my_cursor
        min_database = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="system123",
            database="UniPlanner")

        my_cursor = min_database.cursor()

    def all_students(self, mode='DESC'):
        sql = ("SELECT * FROM Uniplanner.Person WHERE Fornavn = 'Emma'")
        try:
            my_cursor.execute(sql) #håndtering databasen med vores sql-selcelt-statement
            result = my_cursor.fetchall() #hent dataen ift vores sql-statement
        except Exception as error:
            return error

        return result

db = MySQL_connector()
print(db.all_students())


    #Nedenstående bruges til at håndtere forbindelses fejl (erros ift. databasen)
    #Metoden hedder try-except!
    # #https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html





