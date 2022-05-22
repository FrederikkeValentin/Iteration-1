import mysql.connector
from mysql.connector import errorcode

class MySQL_connector:
    """Dette er en class for connecter fra MySQL til Python med 2 attributter"""
    Database_navn = "UniPlanner"
    Forbindelse: mysql.connector.connection
    # Forbindelse er en type
    # Connect er en constructor, der opretter forbindelse til vores database og retunerer et objekt

    def opret_forbindelse_til_databasen(cls): #cls er en class der gør den statisk --> gør det til en class-attribute
        cls.Forbindelse = mysql.connector.connect(user='root',
                                              password='system123',
                                              host='127.0.0.1',
                                              database=cls.Database_navn)

    def get_alt_information(cls):
        min_cursor = cls.Forbindelse.cursor()
        min_cursor.execute("SELECT * FROM Uniplanner.Person WHERE Fornavn = 'Emma'")
        resultat = min_cursor.fetchall()
        print(resultat)

    #Nedenstående bruges til at håndtere forbindelses fejl (erros ift. databasen)
    #Metoden hedder try-except!
    # #https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    def tjek_for_errors():
        try:
            min_database = mysql.connector.connect(user='root',
                                                  database='UniPlanner')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Der er en fejl ved dit brugernavn eller kodeord")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database eksisterer ikke")
            else:
                print(err)
        else:
            min_database.close()




