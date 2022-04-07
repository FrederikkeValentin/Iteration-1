from stdnum.dk import cpr #brug compact

def NyDato(self, date: str, course: str) -> bool:
    AnmodDato = pd.Timestamp(date)
    for key in self.allocatedTimes:
        if (key == AnmodDato):  # The request is already allocated by another course
            return False
    # The requested date is available, we extend our booking with the new request
    self.allocatedTimes[AnmodDato] = course
    return True

def LedigDato(self, date: str) -> bool:
    AnmodDato = pd.Timestamp(date)
    if (AnmodDato in self.allocatedTimes):
        del self.allocatedTimes[AnmodDato]
        return True
    return False

def getAllocations(self) -> Dict[str, str]:
    return self.allocatedTimes


def validate_cpr_nummer():

def validate_login(input_navn: str, max_length: int) -> bool:

def validate_mail

def validate_kodeord