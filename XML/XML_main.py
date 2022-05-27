from Model.Lokale import Lokale
from XML.Writer import LokaleWriter
from XML.Reader import LokaleReader
from Persistence.Database_Connection_MySQL import MySQL_connector

def main():
    """Definerer main"""
    Database_XML = MySQL_connector()
    sql = ("SELECT * FROM Lokale")
    Database_XML.my_cursor.execute(sql)
    Database_Lokale = Database_XML.my_cursor.fetchall()
    liste = []
    for item in Database_Lokale:
        liste.append(Lokale(str(item[0]), str(item[1]), item[2], str(item[3])))

    liste[0].get_lokalenummer()
    Lokale_Writer = LokaleWriter(liste[0])
    Lokale_Writer.save()
        #object.erase()

    inter = LokaleReader().get_Lokale()
    print(inter)   # print("Printing the new contents of the pharmacy")
    # pharmacy.printout()

if __name__ == '__main__':
    main()