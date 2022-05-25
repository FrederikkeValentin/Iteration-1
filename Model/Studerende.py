from datetime import date
from stdnum.dk import cpr

#Private attribute
class Studerende:
    """Dette er en class for underviser"""
    def __init__(self, fornavn: str, efternavn: str, email:str, adresse: str, cpr_nummer: str, studienummer: str, uddannelse: str, semester_el_blok: str, login_uniplanner: str, se_skema: str, modtag_notifikation: str):
        self.__fornavn = fornavn
        self.__efternavn = efternavn
        self.__email = email
        self.__adresse = adresse
        self.__cpr_nummer = cpr_nummer
        self.__studienummer = studienummer
        self.__uddannelse = uddannelse
        self.__semster_el_blok = semester_el_blok
        self.__login_uniplanner = login_uniplanner
        self.__se_skema = se_skema
        self.__modtag_notifikation = modtag_notifikation

    # Nedenstående er getters and setters
    def get_fornavn(self): return self.__fornavn
    def set_fornavn(self, nyt_fornavn): self.__fornavn = nyt_fornavn

    def get_efternavn(self): return self.__efternavn
    def set_efternavn(self, nyt_efternavn): self.__efternavn = nyt_efternavn

    def get_email(self): return self.__email
    def set_email(self, ny_email): self.__email = ny_email

    def get_adresse(self): return self.__adresse
    def set_adresse(self, nyt_adresse): self.__adresse = nyt_adresse

    def get_cpr_nummer(self): return self.__cpr_nummer
    def set_cpr_nummer(self, nyt_cpr_nummer): self.__cpr_nummer = nyt_cpr_nummer

    def get_studienummer(self): return self.__studienummer
    def set_studienummer(self, nyt_studienummer): self.__studienummer = nyt_studienummer

    def get_uddannelse(self): return self.__uddannelse
    def set_uddannelse(self, ny_uddannelse): self.__uddannelse = ny_uddannelse

    def get_semster_el_blok(self): return self.__semster_el_blok
    def set_semster_el_blok(self, nyt_semster_el_blok): self.__semster_el_blok = nyt_semster_el_blok

    def login_uniplanner(self): return self.__login_uniplanner
    def login_uniplanner(self, ny_login_uniplanner): self.__login_uniplanner = ny_login_uniplanner

    def se_skema(self): return self.__se_skema
    def se_skema(self, nyt_se_skema): self.__se_skema = nyt_se_skema

    def modtag_notifikation(self): return self.__modtag_notifikation
    def modtag_notifikation(self, ny_modtag_notifikation): self.__modtag_notifikation = ny_modtag_notifikation

    def __str__(self):
        return f"{self.__fornavn}, {self.__efternavn}, {self.__cpr_nummer}" \
               f", {self.__adresse}, {self.__studienummer},{self.__uddannelse}, " \
               f"{self.__semster_el_blok},{self.__login_uniplanner}, {self.__se_skema}, {self.__modtag_notifikation}"
