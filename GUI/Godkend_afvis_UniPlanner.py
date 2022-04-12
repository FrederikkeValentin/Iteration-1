from PyQt6 import QtWidgets, uic
import sys

class Godkend_afvis_UniPlanner(QtWidgets.QMainWindow):
    """Class for godkend eller afvisning af anmoding fra underviser (set fra sekræterens vinkel)
    Vinduet skal tolkes som en pop-up notifikation/vindue [Anmodninger kan åbnes manuelt] på sekretærens Hovedmenu, med anmodninger fra undervisere om lokaleskift/ændringer!
    Ved flere notifikationer om lokaleskfit/ændringer, vil det fremgå af en liste, som så individiuelt kan trykkes på og godkendes/afvises"""

    def __init__(self):
        super(Godkend_afvis_UniPlanner, self).__init__()
        uic.loadUi('../View/Godkend_afvis_UniPlanner.ui', self)

        self.Godkend_aendring.clicked.connect(self.Godkend_aendring_tryk)
        self.Afvis_aendring.clicked.connect(self.Afvis_aendring_tryk)
        self.show()

    def Godkend_aendring_tryk(self):
        print("Godkend: [trykkes på]")
        print("Anmodning fra underviseren GODKENDES og ændringen vedtages/opdateres "
              "i underviserens, TA's og de studerendes skema (notifikation om lokaleændringer sendes ud!).")
        self.close()

    def Afvis_aendring_tryk(self):
        print("Afvis: [trykkes på]")
        print("Anmodning fra underviseren AFVISES og skemaet forbliver det samme. "
              "Ny anmodning er nødvendig fra underviseren.")
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Godkend_afvis_UniPlanner()
    app.exec()