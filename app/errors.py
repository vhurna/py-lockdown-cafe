# errors.py

class VaccineError(Exception):
    """Base exception for vaccine related errors."""
    pass

class NotVaccinatedError(VaccineError):
    def __init__(self, message="Visitor is not vaccinated"):
        super().__init__(message)

class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Visitor's vaccine is outdated"):
        super().__init__(message)

class NotWearingMaskError(Exception):
    def __init__(self, message="Visitor is not wearing a mask"):
        super().__init__(message)
