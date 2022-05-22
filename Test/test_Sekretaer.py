import Validator
import pytest
from Model.Sekretaer import Sekretaer
#def __init__(self, fornavn: str, efternavn: str, email: str, adresse: str, cpr_nummer: str, titel: str, ansættelses_nr: int):

## TEST
@pytest.fixture
def Sekretær_Uniplanner():

    return Sekretaer("Henning", "Jensen", "hej663@SUND.ku.dk", "Egebjerg 10, 4000 Roskilde", "100181-1968", "Sekretær for SUND", "hej663")

def test_get_efternavn(Sekretær_Uniplanner):

    assert Sekretær_Uniplanner.get_efternavn() == "Jensen"



## FORNAVN
def test_validate_navn_god():
    assert Validator.validate_navn("Henning",80) == True
def test_validate_navn_for_lang():
    assert Validator.validate_navn("Henning",10) == False
def test_validate_navn_for_kort():
    assert Validator.validate_navn("A B") == False
def test_validate_navn_daarligt_format():
    assert Validator.validate_navn("abc !?!") == False

## EFTERNAVN
def test_validate_navn_god():
    assert Validator.validate_navn("Jensen",80) == True
def test_validate_navn_for_lang():
    assert Validator.validate_navn("Jensen",10) == False
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
    assert Validator.validate_titel("Sekretær") == True
def test_validate_titel_daarligt_formst():
    assert Validator.validate_titel("??") == False

## ANSÆTTELSES NR
def test_validate_ansættelses_nr_god():
    assert Validator.validate_ansættelses_nr("789") == True
def test_validate_ansættelses_nr_daarlig():
    assert Validator.validate_ansættelses_nr("syv otte ni") == False
def test_validate_ansættelses_nr_daarlig2():
    assert Validator.validate_ansættelses_nr("000") == False