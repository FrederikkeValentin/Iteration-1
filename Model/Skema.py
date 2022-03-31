class Skema:
    def __init__(self, dato: str, tidspunkt: str, lokale: str, forelæsning: str, kursus: str):
        self.__dato = dato
        self.__tidspunkt = tidspunkt
        self.__lokale = lokale
        self.__forelæsning = forelæsning
        self.__kursus = kursus

    def get_dato(self): return self.__dato
    def set_dato(self, ny_dato): self.__dato = ny_dato

    def get_tidspunkt(self): return self.__tidspunkt
    def set_tidspunkt(self, nyt_tidspunkt): self.__dato = nyt_tidspunkt

    def get_lokale(self): return self.__lokale
    def set_lokale(self, nyt_lokale): self.__dato = nyt_lokale

    def get_forelæsning(self): return self.__forelæsning
    def set_forelæsning(self, ny_forelæsning): self.__dato = ny_forelæsning

    def get_kursus(self): return self.__kursus
    def set_kursus(self, nyt_kursus): self.__dato = nyt_kursus

