from logging import root
import os
from xml.etree import ElementTree
from Model import Lokale


class DispensaryReader:
    __file_name__ = 'Lokale2.xml'
    def __init__(self) -> None:
        full_file = os.path.abspath(os.path.join('data', self.__file_name__))
        dom = ElementTree.parse(full_file)

        #reading general attributes
        root = dom.getroot()
        Adresse = root.attrib['Adresse']
        Lokalenr = root.attrib['Lokalenr']
        Kapacitet= root.attrib['Kapacitet']
        Ledighed = {}

        print ("Ny adresse i ", Adresse)
        #getting all the drugs in stock
        for Ledighed in root.iter('product'):
            lokale_name = Lokale.attrib['lokalenummer']
            print ("vurder ledighed", lokale_name)
            lokale_ledighed = Lokale.attrib['Ledighed']
            Lokale[lokale_ledighed]="JA"
        self.__Lokale__ = Lokale(Adresse, Lokalenr, Kapacitet, Ledighed)

    def getDispensary(self) -> Lokale:
        return self.__Dispensary__