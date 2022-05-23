import Validator
from Model.Underviser import Underviser

## TEST
#def __init__(self, fornavn: str, efternavn: str, email:str, adresse: str, cpr_nummer: str, titel: str, ansættelses_nr: str, kursus:str, login_uniplanner: str, se_skema: str, send_anmodning: str, indberette_tilgængelighed:str):
Hent_underviser = Underviser("Lisbeth", "Lund", "lil789@SUND.ku.dk", "Almevej 7, 2900 Hellerup", "160580-1236", "Underviser påå SUND", "lil786", "Humanbiologi", "lil786", "Yes", "Yes", "Alle ugens dage")

def test_get_ansættelses_nr():
    test = Hent_underviser.get_ansættelses_nr() == "lil786"
    assert test
    print(test) #giver os true eller false


#DETTE ER IKKE RELEVANT, DA VI IKKE HAR EN VALIDATOR
## FORNAVN
def test_validate_navn_god():
    assert Validator.validate_navn("Lisbeth", 80) == True
def test_validate_navn_for_lang():
    assert Validator.validate_navn("Lisbeth", 10) == False
def test_validate_navn_for_kort():
    assert Validator.validate_navn("A B") == False
def test_validate_navn_daarligt_format():
    assert Validator.validate_navn("abc !?!") == False

## EFTERNAVN
def test_validate_navn_god():
    assert Validator.validate_navn("Lund", 80) == True
def test_validate_navn_for_lang():
    assert Validator.validate_navn("Lund", 10) == False
def test_validate_navn_for_kort():
    assert Validator.validate_navn("A B") == False
def test_validate_navn_daarligt_format():
    assert Validator.validate_navn("abc !?!") == False

## EMAIL
def test_validate_email_god():
    assert Validator.validate_email("lil789@SUND.ku.dk") == True
def test_validate_email_daarlig():
    assert Validator.validate_email("lil@SUND.ku.dk") == False
def test_validate_email_daarlig2():
    assert Validator.validate_email("lil789@ku.dk") == False

## ADRESSE
def test_validate_adresse_god():
    assert Validator.validate_adresse("Almevej 7, 2900 Hellerup") == True
def test_validate_adrese_daarlig():
    assert Validator.validate_adresse("Almevej 7, 2900") == False
def test_validate_adrese_daarlig2():
    assert Validator.validate_adresse("Almevej 7, niogtyvehundrede Hellerup") == False

## CPR-NUMMER
def test_validate_cpr_nummer_god():
    assert Validator.validate_cpr_nummer("123456-7891") == True
def test_validate_cpr_nummer_daarligt():
    assert Validator.validate_cpr_nummer("en to tre fire fem seks-syv otte ni ti") == False
def test_validate_cpr_nummer_daarligt2():
    assert Validator.validate_cpr_number("-010490+9995!") == False

## TITEL
def test_validate_titel_god():
    assert Validator.validate_titel("Underviser") == True
def test_validate_titel_daarligt_formst():
    assert Validator.validate_titel("??") == False

## ANSÆTTELSES NR
def test_validate_ansættelses_nr_god():
    assert Validator.validate_ansættelses_nr("789") == True
def test_validate_ansættelses_nr_daarlig():
    assert Validator.validate_ansættelses_nr("syv otte ni") == False
def test_validate_ansættelses_nr_daarlig2():
    assert Validator.validate_ansættelses_nr("000") == False

## KURSUS
def test_validate_kursus_god():
    assert Validator.validate_ansættelses_nr("Humanbiologi") == True
def test_validate_kursus_daarlig():
    assert Validator.validate_ansættelses_nr("SMOA09001U") == False