import Validator

#def __init__(self, kursusnavn: str, kursusID: int, ECTS: float, kursuskapacitet: int, varighed: str, kursusansvarlig: str, andre_undervisere: str, akademisk_grad: str, placering: str, udbydende_institut: str):

## KURSUSNAVN
def test_validate_kursusnavn_god():
    assert Validator.validate_kursusnavn("Aud. Einer Lundsgaard") == True

def test_validate_kursusnavn_daarlig():
    assert Validator.validate_kursusnavn("Auditorium") == False

## KURSUS ID
def test_validate_kursusID_god():
    assert Validator.validate_kursusID("Aud. Einer Lundsgaard") == True

def test_validate_kursusID_daarlig():
    assert Validator.validate_kursusID("Auditorium") == False

## ECTS
def test_validate_ECTS_god():
    assert Validator.validate_ECTS("Aud. Einer Lundsgaard") == True

def test_validate_ECTS_daarlig():
    assert Validator.validate_ECTS("Auditorium") == False

## KURSUSKAPACITET
def test_validate_kursuskapacitet_god():
    assert Validator.validate_kursuskapacitet("Aud. Einer Lundsgaard") == True

def test_validate_kursuskapacitet_daarlig():
    assert Validator.validate_kursuskapacitet("Auditorium") == False

## VARIGHED
def test_validate_varighed_god():
    assert Validator.validate_varighed("Aud. Einer Lundsgaard") == True

def test_validate_varighed_daarlig():
    assert Validator.validate_varighed("Auditorium") == False

## KURSUSANSVARLIG
def test_validate_kursusansvarlig_god():
    assert Validator.validate_kursusansvarlig("Aud. Einer Lundsgaard") == True

def test_validate_kursusansvarlig_daarlig():
    assert Validator.validate_kursusansvarlig("Auditorium") == False

## ANDRE UNDERVISERE
def test_validate_andre_undervisere_god():
    assert Validator.validate_andre_undervisere("Aud. Einer Lundsgaard") == True

def test_validate_andre_undervisere_daarlig():
    assert Validator.validate_andre_undervisere("Auditorium") == False

## AKADEMISK GRAD
def test_validate_akademisk_grad_god():
    assert Validator.validate_akademisk_grad("Aud. Einer Lundsgaard") == True

def test_validate_akademisk_grad_daarlig():
    assert Validator.validate_akademisk_grad("Auditorium") == False

## PLACERING
def test_validate_placering_god():
    assert Validator.validate_placering("Aud. Einer Lundsgaard") == True

def test_validate_placering_daarlig():
    assert Validator.validate_placering("Auditorium") == False

## UDBYDENDE INSTITUT
def test_validate_udbydende_institut_god():
    assert Validator.validate_udbydende_institut("Aud. Einer Lundsgaard") == True

def test_validate_udbydende_institut_daarlig():
    assert Validator.validate_udbydende_institut("Auditorium") == False