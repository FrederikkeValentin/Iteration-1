import mysql.connector
from mysql.connector import errorcode

class MySQL_connector:
    """Dette er en class for connecter fra MySQL til Python med 2 attributter"""
    min_database = None #objekt variabler
    my_cursor = None #objekt variabler

    #OOP - link til hjemmeside hvor koden er fra
    #https://tutspack.com/crud-operation-in-python-with-mysql-using-oop/

    #vores constructor =
    def __init__(self):
        self.min_database = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="system123",
            database="UniPlanner")

        self.my_cursor = self.min_database.cursor()

    def all_students(self, mode='DESC'):
        sql = ("SELECT * FROM Uniplanner.Person WHERE Fornavn = 'Emma'")
        try:
            self.my_cursor.execute(sql) #håndtering databasen med vores sql-selcelt-statement
            result = self.my_cursor.fetchall() #hent dataen ift vores sql-statement
        except Exception as error:
            return error

        return result

    #Nedenstående bruges til at håndtere forbindelses fejl (erros ift. databasen)
    #Metoden hedder try-except!
    # #https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    def tjek_for_errors(self):
        try:
            min_database = mysql.connector.connect(user='root',
                                                   database='UniPlanner')
        except mysql.connector.connect.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Der er noget forkert ved kodeord eller brugernavn")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Databasen eksisterer ikke")
            else:
                print(err)
        else:
            min_database.close()

db = MySQL_connector()
print(db.all_students())



