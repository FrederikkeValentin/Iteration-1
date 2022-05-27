from Model.Studerende import Studerende

## TEST
#def __init__(self, fornavn: str, efternavn: str, email:str, adresse: str, cpr_nummer: str, studienummer: str, uddannelse: str, semester_el_blok: str, login_uniplanner: str, se_skema: str, modtag_notifikation: str):
Hent_studerende = Studerende("Emma", "Frederiksen", "emf876@alumni.ku.dk", "Amager Strandvej 42a, 2300 København S", "040797-1234", "emf876", "Sundhed og Informatik", "4. Semester", "Ja", "Ja", "JA")

def test_get_studienummer():
    test = Hent_studerende.get_studienummer() == "emf876"
    assert test
    print(test) #giver os true eller false