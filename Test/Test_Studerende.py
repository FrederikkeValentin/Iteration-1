from Model.Studerende import Studerende

## TEST
#def __init__(self, fornavn: str, efternavn: str, email:str, adresse: str, cpr_nummer: str, studienummer: str, uddannelse: str, semester_el_blok: str, login_uniplanner: str, se_skema: str, modtag_notifikation: str):
Hent_studerende = Studerende("Lisbeth", "Lund", "lil789@SUND.ku.dk", "Almevej 7, 2900 Hellerup", "160580-1236", "Underviser påå SUND", "lil786", "Humanbiologi", "lil786", "Yes", "Yes", "Alle ugens dage")

def test_get_ansættelses_nr():
    test = Hent_underviser.get_ansættelses_nr() == "lil786"
    assert test
    print(test) #giver os true eller false