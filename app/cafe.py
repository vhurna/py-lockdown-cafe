# cafe.py

import datetime
from .errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if the visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor '{visitor.get('name', 'Unknown')}' is not vaccinated."
            )
        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if expiration_date is None:
            raise NotVaccinatedError(
                f"Visitor '{visitor.get('name', 'Unknown')}' has no valid vaccine information."
            )
        # Check if vaccine is expired
        today = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError(
                f"Visitor '{visitor.get('name', 'Unknown')}' vaccine expired on {expiration_date}."
            )
        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor '{visitor.get('name', 'Unknown')}' is not wearing a mask."
            )
        # All conditions met; allow visiting the cafe.
        return f"Welcome to {self.name}"
