from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *
import sys

#Oprettelse af class for hovedmenuen
class Hovedmenu_UniPlanner(QtWidgets.QMainWindow):
    def __init__(self):
        super(Hovedmenu_UniPlanner, self).__init__()
        uic.loadUi('Hovedmenu_UniPlanner.ui', self)
        layout = QHBoxLayout()

        self.cb = QComboBox()

        #Elementer tilføjes
        self.cb.addItem("Søg")
        self.cb.addItem("Kursus")
        self.cb.addItems(["Hold", "Underviser", "Studerende"])

        #Her connecter min metode "selectionchange" til det valgte element
        self.cb.currentIndexChanged.connect(self.selectionchange)

        #Combobox tilføjes til layout
        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("UniPlanner Hovedmenu")

        #Knappen for: Tilgængelighed
        self.Tilgaengelighed.clicked.connect(self.Tilgaengelighed_tryk)

        #Knappen for: Ændringer/skift af lokale
        self.Lokale_aendringer_skift.clicked.connect(self.Lokale_aendringer_skift_tryk)

        #Knappen for: Næste uge af skemaet
        self.NaesteUge.clicked.connect(self.NaesteUge_tryk)

        #Knappen for: Forrige uge af skemaet
        self.ForrigeUge.clicked.connect(self.ForrigeUge_tryk)

        #Knappen for: Log Ud af Uniplanner
        self.LogUd.clicked.connect(self.LogUd_tryk)

        self.show()

#Def af de forskellige knapper og hvad der sker når man trykker på dem!
    def selectionchange(self, i):
        print("Items in the list are :")
        for count in range(self.cb.count()):
                print(self.cb.itemText(count))
                print("Current index", i, "selection changed ", self.cb.currentText())

    def Tilgaengelighed_tryk(self):
        print("Videre til muligheder for valg af dage man IKKE kan undervise")

    def Lokale_aendringer_skift_tryk(self):
        print("Videre til muligheder for ændringer eller skift af lokale, eventult fjernelse eller tilføjelse")

    def NaesteUge_tryk(self):
        print("Der vises næste uges skema")

    def ForrigeUge_tryk(self):
        print("Der vises forrige uges skema")

    def LogUd_tryk(self):
        self.close()  # Dette vil lukke det hele

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Hovedmenu_UniPlanner()
    app.exec()