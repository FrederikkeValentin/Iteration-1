from datetime import date
from stdnum.dk import cpr

#Private attribute
class Underviser:
    """Dette er en class for underviser"""
    def __init__(self, navn: str, email:str, adresse: str, cpr_nummer: str, titel: str, ansættelses_nr: int, kursus:str):
        self.__navn = navn
        self.__email = email
        self.__adresse = adresse
        self.__cpr_nummer = cpr_nummer
        self.__titel = titel
        self.__ansættelses_nr = ansættelses_nr
        self.__kursus = kursus

    def get_navn(self): return self.__navn
    def set_navn(self, nyt_navn): self.__navn = nyt_navn

    def get_email(self): return self.__email
    def set_email(self, ny_email): self.__email = ny_email

    def get_adresse(self): return self.__adresse
    def set_adresse(self, nyt_adresse): self.__adresse = nyt_adresse

    def get_cpr_nummer(self): return self.__cpr_nummer
    def set_cpr_nummer(self, nyt_cpr_nummer): self.__cpr_nummer = nyt_cpr_nummer

    def get_titel(self): return self.__titel
    def set_titel(self, ny_titel): self.__titel = ny_titel

    def get_ansættelses_nr(self): return self.__ansættelses_nr
    def set_ansættelses_nr(self, nyt_ansættelses_nr): self.__ansættelses_nr = nyt_ansættelses_nr

    def get_kursus(self): return self.__kursus
    def set_kursus(self, nyt_kursus): self.__kursus = nyt_kursus

    #Alder er udregnet ved hjælp af CPR-nummeret, derfor skal der ikke være set
    def get_alder(self):
        __cpr_compact = cpr.compact(self.__cpr_nummer)
        __dato_idag = date.today()
        __fødsels_information = cpr.get_fødsels_information(__cpr_compact)
        __alder_dato = __dato_idag - __fødsels_information
        return int(__alder_dato.days / 365.2425)

    def __str__(self):
        return f"{self.__navn}, {self.__cpr_nummer}" \
               f", {self.__adresse}, {self.__titel},{self.__ansættelses_nr}, {self.__kursus} age: {self.get_alder()} years"