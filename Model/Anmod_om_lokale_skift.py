class Anmod_om_lokale_skift:
    """Dette er en class for anmod om lokaleskift"""
    def __init__(self, dato: str, tidspunkt: str, lokale: str, forelæsning: str, kursus: str, nuvaerende_lokale: str, ledige_lokaler: str, anmodning: str):
        self.__dato = dato
        self.__tidspunkt = tidspunkt
        self.__lokale = lokale
        self.__forelæsning = forelæsning
        self.__kursus = kursus
        self.__nuvaerende_lokale = nuvaerende_lokale
        self.__ledige_lokaler = ledige_lokaler
        self.__anmodning = anmodning

# Nedenstående er getters and setters
    def get_dato(self): return self.__dato
    def set_dato(self, ny_dato): self.__dato = ny_dato

    def get_tidspunkt(self): return self.__tidspunkt
    def set_tidspunkt(self, nyt_tidspunkt): self.__tidspunkt = nyt_tidspunkt

    def get_lokale(self): return self.__lokale
    def set_lokale(self, nyt_lokale): self.__lokale = nyt_lokale

    def get_forelæsning(self): return self.__forelæsning
    def set_forelæsning(self, ny_forelæsning): self.__forelæsning = ny_forelæsning

    def get_kursus(self): return self.__kursus
    def set_kursus(self, nyt_kursus): self.__kursus = nyt_kursus

    def get_nuvaerende_lokale(self): return self.__nuvaerende_lokale
    def set_nuvaerende_lokale(self, nyt_nuvaerende_lokale): self.__nuvaerende_lokale = nyt_nuvaerende_lokale

    def get_ledige_lokaler(self): return self.__ledige_lokaler
    def set_ledige_lokaler(self, nye_ledige_lokaler): self.__ledige_lokaler = nye_ledige_lokaler

    def get_anmodning(self): return self.__anmodning
    def set_anmodning(self, ny_anmodning): self.__anmodning = ny_anmodning

    def __str__(self):
        return f"{self.__dato}, {self.__tidspunkt}" \
               f", {self.__lokale}, {self.__forelæsning},{self.__kursus}, " \
               f"{self.__nuvaerende_lokale}, {self.__ledige_lokaler}, {self.__anmodning}"



