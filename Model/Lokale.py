class Lokale:
    """Dette er en class for sekretær"""
    def __init__(self, adresse: str, lokalenummer: str, kapacitet: int, ledighed: str):
        self.__adresse = adresse
        self.__lokalenummer =lokalenummer
        self.__kapacitet = kapacitet
        self.__ledighed = ledighed

    list_ledige_lokaler = []

    def __str__(self):
        return f"{self.__adresse}, {self.__lokalenummer}" \
               f", {self.__kapacitet}, {self.__ledighed}"


