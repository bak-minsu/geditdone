from geditdone.gedcom_objects import GedcomError

def marriage_before_divorce(parser):
    """Makes sure marriage come before a divorce"""
    families = parser.families
    errors = []

    for family in families.values():
        if family.married is not None and \
            family.divorced is not None and \
            family.married >= family.divorced:
                errorMessage = f'Marriage date {family.married} is after divorce date {family.divorced}'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US04', family, errorMessage))
        elif family.married is None and family.divorced is not None:
                errorMessage = f'Marriage date is None while divorce date is not.'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US04', family, errorMessage))

    return errors