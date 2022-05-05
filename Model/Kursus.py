class Kursus:
    """Dette er en class for kursus"""
    def __init__(self, kursusnavn: str, kursusID: int, ECTS: float, kursuskapacitet: int, varighed: str, kursusansvarlig: str, andre_undervisere: str, akademisk_grad: str, placering: str, udbydende_institut: str):
        self.__kursusnavn = kursusnavn
        self.__kursusID = kursusID
        self.__ECTS = ECTS
        self.__kursuskapacitet = kursuskapacitet
        self.__varighed = varighed
        self.__kursusansvarlig = kursusansvarlig
        self.__andre_undervisere = andre_undervisere
        self.__akademisk_grad = akademisk_grad
        self.__placering = placering
        self.__udbydende_institut = udbydende_institut

# Nedenstående er getters and setters
    def get_kursusnavn(self): return self.__kursusnavn
    def set_kursusnavn(self, nyt_kursusnavn): self.__kursusnavn = nyt_kursusnavn

    def get_kursusID(self): return self.__kursusID
    def set_kursusID(self, nyt_kursusID): self.__kursusID = nyt_kursusID

    def get_ECTS(self): return self.__ECTS
    def set_ECTS(self, nye_ECTS): self.__ECTS = nye_ECTS

    def get_kursuskapacitet(self): return self.__kursuskapacitet
    def set_kursuskapacitet(self, nyt_kursuskapacitet): self.__kursuskapacitet = nyt_kursuskapacitet

    def get_varighed(self): return self.__varighed
    def set_varighed(self, nyt_varighed): self.__varighed = nyt_varighed

    def get_kursusansvarlig(self): return self.__kursusansvarlig
    def set_kursusansvarlig(self, ny_kursusansvarlig): self.__kursusansvarlig = ny_kursusansvarlig

    def get_andre_undervisere(self): return self.__andre_undervisere
    def set_andre_undervisere(self, nye_andre_undervisere): self.__andre_undervisere = nye_andre_undervisere

    def get_akademisk_grad(self): return self.__akademisk_grad
    def set_akademisk_grad(self, ny_akademisk_grad): self.__akademisk_grad = ny_akademisk_grad

    def get_placering(self): return self.__placering
    def set_placering(self, ny_placering): self.__placering = ny_placering

    def get_udbydende_institut(self): return self.__udbydende_institut
    def set_udbydende_institut(self, nyt_udbydende_institut): self.__udbydende_institut = nyt_udbydende_institut

    def __str__(self):
        return f"{self.__kursusnavn}, {self.__kursusID}" \
               f", {self.__ECTS}, {self.__kursuskapacitet},{self.__varighed}, " \
               f"{self.__kursusansvarlig}, {self.__andre_undervisere}, {self.__akademisk_grad}, " \
               f"{self.__placering}, {self.__udbydende_institut}"