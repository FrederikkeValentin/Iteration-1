class Lokale:
    """Dette er en class for lokale"""
    def __init__(self, adresse: str, lokalenummer: str, kapacitet: int, ledighed: str):
        self.__adresse = adresse
        self.__lokalenummer =lokalenummer
        self.__kapacitet = kapacitet
        self.__ledighed = ledighed

    list_ledige_lokaler = []

    def get_adresse(self): return self.__adresse
    def set_adresse(self, nyt_adresse): self.__adresse = nyt_adresse

    def get_lokalenummer(self): return self.__lokalenummer
    def set_lokalenummer(self, nyt_lokalenummer): self.__lokalenummer = nyt_lokalenummer

    def get_kapacitet(self): return self.__kapacitet
    def set_kapacitet(self, ny_kapacitet): self.__kapacitet = ny_kapacitet

    def get_ledighed(self): return self.__ledighed
    def set_ledighed(self, nyt_ledighed): self.__ledighed = nyt_ledighed

    def __str__(self):
        return f"{self.__adresse}, {self.__lokalenummer}" \
               f", {self.__kapacitet}, {self.__ledighed}"


