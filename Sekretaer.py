class Underviser:
    def __init__(self, navn: str, email: str, adresse: str, cpr_nummer: str, titel: str, ansættelses_nr: int):
        self.__navn = navn
        self.__email = email
        self.__adresse = adresse
        self.__cpr_nummer = cpr_nummer
        self.__titel = titel
        self.__ansættelses_nr = ansættelses_nr

    def get_navn(self): return self.__navn
    def set_navn(self, nyt_navn): self.__navn = nyt_navn

    def get_email(self): return self.__email
    def set_email(self, ny_email): self.__email = ny_email

    def get_adresse(self): return self.__adresse
    def set_adresse(self, nyt_adresse): self.__adresse = nyt_adresse

    def get_cpr_nummer(self): return self.__cpr_nummer
    def set_cpr_nummer(self, nyt_cpr_nummer): self.__cpr_nummer = nyt_cpr_nummer

    def get_titel(self): return self.__titel
    def set_titel(self, ny_titel): self.__email = ny_titel

    def get_ansættelses_nr(self): return self.__ansættelses_nr
    def set_ansættelses_nr(self, nyt_ansættelses_nr): self.__email = nyt_ansættelses_nr
