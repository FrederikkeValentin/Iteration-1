from PyQt6 import QtWidgets, uic
import sys
import Skema

class Lokaleaendringer_UniPlanner(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lokaleaendringer_UniPlanner, self).__init__()
        uic.loadUi('Lokaleaendringer_UniPlanner.ui', self)

        self.Send_anmodning.clicked.connect(self.Send_anmodning_tryk)
        self.show()

    def Send_anmodning_tryk(self):
        print("Send anmodning trykkes på!")
        liste_skema=[]
        skema = Skema("15-02-22", "9-10", "Aud. Einer Lundsgaard", "Endokrine Sygdomme", "Humanbiologi")
        liste_skema.append(skema)
        print(skema)
        print("ændrer lokale")
        skema.set_lokale("Aud. Niels K. Jerne")
        print(skema)
        self.close()  # This will close the main GUI

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Lokaleaendringer_UniPlanner()
    app.exec()