import os
from xml.etree.ElementTree import ElementTree, tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom

from Model import Lokale


class LokaleWriter:
    def __init__(self, d: Lokale) -> None:
        print("Writing root nodes")
        self.__root__ = ET.Element("Lokale")
        self.__root__.set("Adresse", d.getAdresse())
        self.__root__.set("Lokalenr", d.getLokalenr())
        self.__root__.set("Kapacitet", d.getKapacitet())
        self.__stock__ = ET.SubElement(self.__root__, "Ledighed")
        for Lokale in d.getLedighed():
            ET.SubElement(self.__stock__, "Lokale", {'name': Lokale, 'quantity': str(d.get()[Lokale])})
        print (tostring(self.__root__))
    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        print (tree)
        # prettyTree = prettify(tree)
        # print (prettyTree)
        tree.write("Lokale.xml")

def prettify(elem):
    """Return a pretty-printed XML string for the element.
    """
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")