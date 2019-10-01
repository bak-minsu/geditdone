from geditdone.gedcom_objects import GedcomError
from datetime import date

def dates_before_current_date(parser):
    """Makes sure all dates are before current date"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    current_date = date.today()

    # check all individual dates: birth, death
    for individual in individuals.values():
        if individual.birth is not None and individual.death is not None:
            if individual.birth >= current_date:
                errorMessage = f'Birth date {individual.birth} occurs in the future'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US01', individual, errorMessage))
            elif individual.death >= current_date:
                errorMessage = f'Death date {individual.birth} occurs in the future'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US01', individual, errorMessage))

    # check all family dates: marriage, divorce
    for family in families.values():
        if family.married is not None and family.divorced is not None:
            if family.married >= current_date:
                errorMessage = f'Marriage date {individual.birth} occurs in the future'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US01', family, errorMessage))
            elif family.divorced >= current_date:
                errorMessage = f'Divorce date {individual.birth} occurs in the future'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US01', family, errorMessage))

    return errors