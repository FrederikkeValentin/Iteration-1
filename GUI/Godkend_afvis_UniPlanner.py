from PyQt6 import QtWidgets, uic
import sys

class Godkend_afvis_UniPlanner(QtWidgets.QMainWindow):
    """Class for godkend eller afvisning af anmoding fra underviser (vinduet) - for sekræteren"""
    def __init__(self):
        super(Godkend_afvis_UniPlanner, self).__init__()
        uic.loadUi('../View/Godkend_afvis_UniPlanner.ui', self)

        self.Godkend_aendring.clicked.connect(self.Godkend_aendring_tryk)
        self.Afvis_aendring.clicked.connect(self.Afvis_aendring_tryk)
        self.show()

    def Godkend_aendring_tryk(self):
        print("Godkend: [trykkes på]")
        print("Anmodning fra underviseren GODKENDES og ændringen vedtages/opdateres "
              "i underviserens, TA's og de studerendes skema.")
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