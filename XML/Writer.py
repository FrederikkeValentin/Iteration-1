import os
from xml.etree.ElementTree import ElementTree, tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom

from Model.Lokale import Lokale


class LokaleWriter:
    def __init__(self, l: Lokale) -> None:

        self.__root__ = ET.Element("Lokale")
        self.__root__.set("adresse", l.get_adresse())
        self.__root__.set("lokalenummer", l.get_lokalenummer())
        self.__root__.set("kapacitet", l.get_kapacitet())
        self.__root__.set("ledighed", l.get_ledighed())

        #self.__available__ = ET.SubElement(self.__root__, "Available")
        #for course in l.getAvailable():
        #    ET.SubElement(self.__available__, "course", {'name': course, 'room': str(l.getAvailable()[course])})
        #    print(tostring(self.__root__))

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        tree.write("../XLM/lokaledata.xml")


def prettify(elem):
    """retunerer en pretty-printed XML string"""
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparesed = minidom.parseString(rough_string)
    return reparesed.topprettyxml(indent="  ")