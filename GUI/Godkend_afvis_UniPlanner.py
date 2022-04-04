from PyQt6 import QtWidgets, uic
import sys

class Godkend_afvis_UniPlanner(QtWidgets.QMainWindow):
    def __init__(self):
        super(Godkend_afvis_UniPlanner, self).__init__()
        uic.loadUi('Godkend_afvis_UniPlanner.ui', self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Godkend_afvis_UniPlanner()
    app.exec()