from PyQt6 import QtWidgets, uic
import sys


class Lokaleaendringer_UniPlanner(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lokaleaendringer_UniPlanner, self).__init__()
        uic.loadUi('Lokaleaendringer_UniPlanner.ui', self)

        self.Send_anmodning.clicked.connect(self.Send_anmodning_tryk)
        self.show()

    def Send_anmodning_tryk(self):
        print("Send anmodning [trykkes på]")
        self.close()  # This will close the main GUI

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Lokaleaendringer_UniPlanner()
    app.exec()