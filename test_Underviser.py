import validator

def test_fornavn_god():
    assert validator.validate_name("Lisbeth Lund",80) == True

def test_fornavn_for_lang():
    assert validator.validate_name("Lisbeth Lund",10) == False

def test_validate_name_for_kort():
    assert validator.validate_name("A B",10) == False

def test_validate_name_daarligt_format():
    assert validator.validate_name("abc !?!",20) == False

def test_validate_cpr_nummer_god():
    assert validator.validate_cpr_nummer("123456-7891") == True

def test_cpr_nummer_name_daarligt():
    assert validator.validate_cpr_nummer("en to tre fire fem seks-syv otte ni ti") == False

def test_validate_mobilnummer_god():
    assert validator.validate_street_number("12345678") == True

def test_validate_mobilnummer_daarligt():
    assert validator.validate_street_number("0000000") == False

def test_validate_mobilnummer_daarligt_2():
    assert validator.validate_street_number("XIV") == False


def test_validate_zip_code_good():
    assert validator.validate_zip_code("2820") == True


def test_validate_zip_code_good():
    assert validator.validate_zip_code("2820") == True


def test_validate_zip_code_bad():
    assert validator.validate_zip_code("12820") == False

def test_validate_zip_code_badformat():
    assert validator.validate_zip_code("#1820") == False


def test_validate_city_name():
    assert validator.validate_city_name("Gentofte") == True


def test_validate_city_name():
    assert validator.validate_city_name("Æble_grød_213-.¤2") == False



# The next two tests will only work with a valid cpr number!
# e.g. try it on your own laptop with your own cpr-number

#def test_validate_cpr_number_good():
#    assert validator.validate_cpr_number("xxxxxx-yyyy") == True
#
#
#def test_validate_cpr_number_good2():
#    assert validator.validate_cpr_number("xxxxxxyyyy") == True
#

def test_validate_cpr_number_bad():
    assert validator.validate_cpr_number("-010490+9995!") == False