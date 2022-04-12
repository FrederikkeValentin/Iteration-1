from PyQt6 import QtWidgets, uic
import sys
from GUI.Hovedmenu import Hovedmenu_UniPlanner

class Login(object):
    """This is the system model"""
    login = False

    @classmethod
    def get_login(cls):
        return cls.login
    @classmethod
    def set_login(cls, l):
        cls.login = l

class Model(object):
    """This is the system model"""
    current_user = None
    class_list =  []

    @classmethod
    def set_current_user(cls, user):
        cls.current_user = user
    @classmethod
    def get_current_user(cls):
        return cls.current_user

class Login_UniPlanner(QtWidgets.QMainWindow):
    """Class for Loginvinduet (set fra alles vinkel)
    Der kræves UNI-mail og 4-cifret (tal) kode for at logge ind i UniPlanner"""

    def __init__(self):
        super(Login_UniPlanner, self).__init__()
        uic.loadUi('../View/Login_UniPlanner.ui', self)

        self.Login_knap.clicked.connect(self.Login_knap_tryk)
        self.show()

    def Login_knap_tryk(self):
        print(self.Mail_felt.text())
        print(self.Kodeord_felt.text())
        print("Succesfuldt logget ind i: UniPlanner")

        Login.set_login(True)
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login_UniPlanner()
    app.exec()
    if Login.get_login() is True:
        print("Videre til Hovedmenu")
        vindue2 = Hovedmenu_UniPlanner()
        app.exec()