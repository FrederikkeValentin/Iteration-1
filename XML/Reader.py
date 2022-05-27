from logging import root
import os
from xml.etree import ElementTree
from Model.Lokale import Lokale

class LokaleReader:
    __file_name__ = 'lokaledata.xml'

    def __init__(self):
        full_file = os.path.abspath(os.path.join('data', self.__file_name__))
        print(str(full_file))
        dom = ElementTree.parse(full_file)

        root = dom.getroot()
        adresse = root.attrib['adresse']
        lokalenummer = root.attrib['lokalenummer']
        kapacitet = root.attrib['kapacitet']
        ledighed = root.attrib['ledighed']

        print("Nyt lokale i", lokalenummer)

        self.__Lokale__ = Lokale(adresse, lokalenummer, kapacitet, ledighed)

    def get_Lokale(self) -> Lokale:
        return self.__Lokale__