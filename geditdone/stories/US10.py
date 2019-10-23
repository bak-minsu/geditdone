from geditdone.gedcom_objects import GedcomError
from geditdone.datehelpers import DateHelpers

def marriage_after_14(parser):
    """Returns errors for individuals married before the age of 14"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for fam in families.values():
        if fam.married:
            if fam.husband_id:
                husband = individuals.get(fam.husband_id)
                if husband and husband.birth and \
                    DateHelpers.dates_within(husband.birth, fam.married, 14, 'years'):
                        errorMessage = f'Married {fam.married} before husband turned 14 {husband.birth}'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US10', fam, errorMessage))
            if fam.wife_id:
                wife = individuals.get(fam.wife_id)
                if wife and wife.birth and \
                    DateHelpers.dates_within(wife.birth, fam.married, 14, 'years'):
                        errorMessage = f'Married {fam.married} before wife turned 14 {wife.birth}'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US10', fam, errorMessage))

    return errors