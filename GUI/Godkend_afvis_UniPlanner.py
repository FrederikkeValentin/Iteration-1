from PyQt6 import QtWidgets, uic
import sys

class Godkend_afvis_UniPlanner(QtWidgets.QMainWindow):
    """Class for godkend eller afvisning af anmoding fra underviser (set fra sekræterens vinkel)
    Vinduet skal tolkes som en pop-up notifikation/vindue [Anmodninger kan åbnes manuelt] på sekretærens Hovedmenu, med anmodninger fra undervisere om lokaleskift/ændringer!
    Ved flere notifikationer om lokaleskfit/ændringer, vil det fremgå af en liste, som så individiuelt kan trykkes på og godkendes/afvises"""

    def __init__(self):
        super(Godkend_afvis_UniPlanner, self).__init__()
        uic.loadUi('../View/Godkend_afvis_UniPlanner.ui', self)

        #Knappen for: GODKEND ÆNDRNG
        self.Godkend_aendring.clicked.connect(self.Godkend_aendring_tryk)

        #Knappen for: AFVIS ÆNDRING
        self.Afvis_aendring.clicked.connect(self.Afvis_aendring_tryk)

        #Knappen for: Log Ud af Uniplanner
        self.LogUd.clicked.connect(self.LogUd_tryk)

        self.show()

    #Def af de forskellige knapper og hvad der sker når man trykker på dem!
    #GODKEND ÆNDRNG
    def Godkend_aendring_tryk(self):
        print("Godkend: [trykkes på]")
        print("Anmodning fra underviseren GODKENDES og ændringen vedtages/opdateres "
              "i underviserens, TA's og de studerendes skema (notifikation om lokaleændringer sendes ud!).")
        self.close()

        button = QtWidgets.QMessageBox.question(self, "Hurtig bemærkning:",
                                                "Bekræft at du vil GODKENDE anmodingen om lokaleskift fra: Lisbeth Lund")
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes, GODKEND anmodning!")
        else:
            print("Return")

    #AFVIS ÆNDRING
    def Afvis_aendring_tryk(self):
        print("Afvis: [trykkes på]")
        print("Anmodning fra underviseren AFVISES og skemaet forbliver det samme. "
              "Ny anmodning er nødvendig fra underviseren.")
        self.close()

        button = QtWidgets.QMessageBox.question(self, "Hurtig bemærkning:",
                                                "Bekræft at du vil AFVISE anmodingen om lokaleskift fra: Lisbeth Lund")
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes, AFVIS anmodning!")
        else:
            print("Return")

    #LOG UD
    def LogUd_tryk(self):
        self.close()  # Dette vil lukke det hele

#Starter app-vinduet
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Godkend_afvis_UniPlanner()
    app.exec()