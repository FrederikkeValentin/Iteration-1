from PyQt6 import QtWidgets, uic
import sys

class Lokaleaendringer_UniPlanner(QtWidgets.QMainWindow):
    """Class for Lokaleændringer vinduet (set fra underviserens vinkel.
    Her har en underviser mulighed for at anmode om lokaleskift/ændringer til fx en forelæsning
    Det er sekretæren som skal godkende eller afvise den pågældende anmondning i hendes egen UniPlanner (se: Godkend_afvis_UniPlanner))"""

    def __init__(self):
        super(Lokaleaendringer_UniPlanner, self).__init__()
        uic.loadUi('../View/Lokaleaendringer_UniPlanner.ui', self)

        self.Send_anmodning.clicked.connect(self.Send_anmodning_tryk)
        self.show()

    def Send_anmodning_tryk(self):
        print("Send anmodning [trykkes på]")
        self.close()  # This will close the main GUI

        button = QtWidgets.QMessageBox.question(self, "Hurtig bemærkning", "Bekræft at du vil sende en anmoding om lokaleskift" "Ved lang svartid, skal du sende en ny")
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes, send anmodning!")
        else:
            print("No. Jeg dobbelttjekker lige min anmodning!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Lokaleaendringer_UniPlanner()
    app.exec()