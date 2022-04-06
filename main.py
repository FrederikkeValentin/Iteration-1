from Model import Skema, Anmod_om_lokale_skift

def main():
        liste_skema=[]
        nuvaerende_lokale = Skema("15-02-22", "9-10", "Aud. Einer Lundsgaard", "Endokrine Sygdomme", "Humanbiologi")
        liste_skema.append(nuvaerende_lokale)
        print(nuvaerende_lokale)

        print("ændrer lokale")

        ledigt_lokale = Skema("15-02-22", "9-10", "Aud. Niels K. Jerne", "Endokrine Sygdomme", "Humanbiologi")
        liste_skema.append(ledigt_lokale)
        print(ledigt_lokale)

        app = QtWidgets.QApplication(sys.argv)
        anmod_om_lokale_skift_vindue = Anmod_om_lokale_skift(liste_skema)
        app.exec()

if __name__ == '__main__':
    main()