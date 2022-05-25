#Private attribute
class Sekretaer:
    """Dette er en class for sekretær"""
    def __init__(self, fornavn: str, efternavn: str, email: str, adresse: str, cpr_nummer: str, titel: str, login_uniplanner: str, se_skema: str, ansættelses_nr: str):
        self.__fornavn = fornavn
        self.__efternavn = efternavn
        self.__email = email
        self.__adresse = adresse
        self.__cpr_nummer = cpr_nummer
        self.__titel = titel
        self.__login_uniplanner = login_uniplanner
        self.__se_skema = se_skema
        self.__ansættelses_nr = ansættelses_nr

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

    def get_titel(self): return self.__titel
    def set_titel(self, ny_titel): self.__titel = ny_titel

    def login_uniplanner(self): return self.__login_uniplanner
    def login_uniplanner(self, ny_login_uniplanner): self.__login_uniplanner = ny_login_uniplanner

    def se_skema(self): return self.__se_skema
    def se_skema(self, nyt_se_skema): self.__se_skema = nyt_se_skema

    def get_ansættelses_nr(self): return self.__ansættelses_nr
    def set_ansættelses_nr(self, nyt_ansættelses_nr): self.__email = nyt_ansættelses_nr

    def __str__(self):
        return f"{self.__fornavn}, {self.__efternavn}, {self.__email}" \
               f", {self.__adresse}, {self.__cpr_nummer}, {self.__titel}," \
               f"{self.__login_uniplanner},{self.__se_skema},{self.__ansættelses_nr}"