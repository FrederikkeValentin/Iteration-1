from PyQt6 import QtWidgets, uic
import sys

class Lokaleaendringer_UniPlanner(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lokaleaendringer_UniPlanner, self).__init__()  # MyFirstAppUi must be the same as the name of the class
        uic.loadUi('Lokaleaendringer_UniPlanner.ui', self)  # MyFirstAppGUI.ui is the name of your ui file

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Lokaleaendringer_UniPlanner()
    app.exec()