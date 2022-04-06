from PyQt6 import QtWidgets, uic
import sys
from GUI import Hovedmenu


class Login_UniPlanner(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login_UniPlanner, self).__init__()
        uic.loadUi('../View/Login_UniPlanner.ui', self)

        self.Login_knap.clicked.connect(self.Login_knap_tryk)

        self.show()

    def Login_knap_tryk(self):
        print(self.Mail_felt.text())
        print(self.Kodeord_felt.text())
        print("Videre til hovedmenu")
        if self.w is None:
            self.w = Hovedmenu()
            self.w.show()
        else:
            self.show()

    def show_new_window(self, checked):
        self.w = Hovedmenu()
        self.w.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login_UniPlanner()
    app.exec()