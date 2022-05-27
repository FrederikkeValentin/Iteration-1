from Model.Lokale import Lokale

## TEST
#def __init__(self, adresse: str, lokalenummer: str, kapacitet: int, ledighed: str):

Hent_ledighed= Lokale("Blegdamsvej 3B, 2200 København N", "Aud. Einer Lundsgaard", 100, "JA")

def test_get_ledighed():
    test = Hent_ledighed.get_ledighed() == "JA"
    assert test
    print(test) #giver os true eller false