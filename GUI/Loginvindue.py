from PyQt6 import QtWidgets, uic
import sys
from Persistence import Database_Connection_MySQL
from GUI.Hovedmenu import Hovedmenu_UniPlanner

class Login(object):
    """This is the system model"""
    login = False

    @classmethod
    def get_login(cls):
        return cls.login
    @classmethod
    def set_login(cls, l):
        cls.login = l #l er en parameter

class Login_UniPlanner(QtWidgets.QMainWindow):
    """Class for Loginvinduet (set fra alles vinkel)
    Der kræves UNI-mail og 4-cifret (tal) kode for at logge ind i UniPlanner"""

    def __init__(self):
        super(Login_UniPlanner, self).__init__()
        uic.loadUi('../View/Login_UniPlanner.ui', self)

        # Knappen for: Login
        self.Login_knap.clicked.connect(self.Login_knap_tryk) #self referer til objektet selv

        self.show()

    #Def af de forskellige knapper og hvad der sker når man trykker på dem!
    #LOGIN KNAP
    def Login_knap_tryk(self):
        Mail_felt = self.Mail_felt.text()
        print(self.Mail_felt.text())
        Kodeord_felt = self.Kodeord_felt.text()
        print(self.Kodeord_felt.text())
        #verificer_bruger = Database_Connection.check_kordeord(Mail_felt, Kodeord_felt)
        #if verificer_bruger == True:
        #    print("Succesfuldt logget ind i: UniPlanner")
        #else:
        #    print("fejl")

        Login.set_login(True)
        self.close()

#Starter app-vinduet
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login_UniPlanner()
    app.exec()
    if Login.get_login() is True:
        print("Videre til Hovedmenuen for underviseren")
        vindue2 = Hovedmenu_UniPlanner()
        app.exec()