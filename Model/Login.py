#Private attribute
class Login:
    """Dette er en class for login-siden"""
    def __init__(self, brugernavn: str, adgangskode: str, valider_bruger: str):
        self.__brugernavn = brugernavn
        self.__adgangskode = adgangskode
        self.__valider_bruger = valider_bruger

    def __str__(self):
        return f"{self.__brugernavn}, {self.__adgangskode}", {self.__valider_bruger}"