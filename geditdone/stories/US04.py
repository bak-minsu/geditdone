from geditdone.gedcom_objects import GedcomError

def marriage_before_divorce(parser):
    """Makes sure marriage come before a divorce"""
    families = parser.families
    errors = []

    for family in families.values():
        if family.married is not None and \
            family.divorced is not None and \
            family.married >= family.divorced:
                errorMessage = f''
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US04', family, "Marriage after divorce"))
        elif family.married is None and family.divorced is not None:
                errorMessage = f''
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US04', family, "Marriage after divorce"))

    return errors