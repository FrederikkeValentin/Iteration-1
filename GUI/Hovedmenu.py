from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
import sys
from GUI.Lokaleaendringer import Lokaleaendringer_UniPlanner

#CONTROLLER CLASS
class Hovedmenu_UniPlanner(QtWidgets.QMainWindow):
    """Class for Hovedmenu vinduet (set fra underviserens vinkel)
    Hovedmenuen indeholder menupunkt med valgmuligheder = (mine anmodninger, søg, kurser, studerende og underviser),
    mulighed for indberettlse af ledighed og ændringer i skemaet med henblik på lokaleskfit/ændringer"""

    def __init__(self):
        super(Hovedmenu_UniPlanner, self).__init__()
        uic.loadUi('../View/Hovedmenu_UniPlanner.ui', self)
        layout = QHBoxLayout()

        self.cb = QComboBox()

        #Elementer tilføjes
        self.cb.addItem("Mine anmodninger (skift af lokale)")
        self.cb.addItem("Søg")
        self.cb.addItem("Kursus")
        self.cb.addItems(["Hold", "Underviser", "Studerende"])

        #Her connecter jeg min metode "dropdown", til det valgte element
        self.cb.currentIndexChanged.connect(self.dropdown)

        #Combobox tilføjes til layout
        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("UniPlanner Hovedmenu")

        #Knappen for: Tilgængelighed
        self.Tilgaengelighed.clicked.connect(self.Tilgaengelighed_tryk)

        #Knappen for: Ændringer/skift af lokale
        self.Lokale_aendringer_skift.clicked.connect(self.Lokale_aendringer_skift_tryk)

        #Knappen for: Log Ud af Uniplanner
        self.LogUd.clicked.connect(self.LogUd_tryk)

        self.show()

#Def af de forskellige knapper og hvad der sker når man trykker på dem!
    #DROPDOWN
    def dropdown(self, i):
        for count in range(self.cb.count()):
                print(self.cb.itemText(count))

    #TILGÆNGELIGHED
    def Tilgaengelighed_tryk(self):
        print("Videre til muligheder for valg af dage man IKKE kan undervise")

    #LOKALE ÆNDRINGER
    def Lokale_aendringer_skift_tryk(self):
        print("Videre til muligheder for ændringer eller skift af lokale, eventult fjernelse eller tilføjelse")
        self.lokale_skift = Lokaleaendringer_UniPlanner()
        self.lokale_skift.show()

    #LOG UD
    def LogUd_tryk(self):
        self.close()  #Dette vil lukke det hele

#Starter app-vinduet
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Hovedmenu_UniPlanner()
    app.exec()