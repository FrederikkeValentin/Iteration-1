import Validator
from Model.Skema import Skema

## TEST
#def __init__(self, dato: str, tidspunkt: str, lokale: str, forelæsning: str, kursus: str):
Hent_ledige_lokaler= Skema("Tirsdag d. 15. Marts", "09:15-10:00", "Aud. Niels K. Jerne", "Endokrine Sygdomme", "Humanbiologi")

def test_get_lokale():
    test = Hent_ledige_lokaler.get_lokale() == "Aud. Niels K. Jerne"
    assert test
    print(test) #giver os true eller false


#DETTE ER IKKE RELEVANT, DA VI IKKE HAR EN VALIDATOR
## DATO
def test_validate_dato_god():
    assert Validator.validate_dato("Tirsdag d. 15. Marts") == True
def test_validate_dato_god():
    assert Validator.validate_dato("15/03/2022") == True
def test_validate_dato_daarlig():
    assert Validator.validate_dato("Tirsdag d. et-fem marts") == False

## TIDSPUNKT
def test_validate_tidspunkt_god():
    assert Validator.validate_tidspunkt("Kl. 9") == True
def test_validate_tidspunkt_god():
    assert Validator.validate_tidspunkt("9") == True
def test_validate_tidspunkt_daarlig():
    assert Validator.validate_tidspunkt("Ni") == False

## LOKALE
def test_validate_lokale_god():
    assert Validator.validate_lokale("Aud. Einer Lundsgaard") == True
def test_validate_lokale_daarlig():
    assert Validator.validate_lokale("Auditorium") == False

## FORELÆSNING
def test_validate_forelæsning_god():
    assert Validator.validate_forelæsning("Endokrine Sygdomme") == True
def test_validate_forelæsning_god():
    assert Validator.validate_forelæsning("Endokrine sygdomme") == True
def test_validate_forelæsning_slang():
    assert Validator.validate_forelæsning("Endo") == False

## KURSUS
def test_validate_kursus_god():
    assert Validator.validate_kursus("Humanbiologi") == True
def test_validate_kursus_slang():
    assert Validator.validate_kursus("Human") == False