from geditdone.error_objects import GedcomError, ErrorType

def no_married_siblings(parser):
    """Returns errors for siblings who are married"""
    families = parser.families
    errors = []

    for fam in families.values():
        if fam.husband_id and fam.wife_id:
            sublist = [fam.husband_id, fam.wife_id]
            for check_fam in families.values():
                if check_fam.child_ids:
                    if all(x in check_fam.child_ids for x in sublist):
                        errorMessage = f'Siblings {fam.husband_id} and {fam.wife_id} of {check_fam} are married in {fam}'
                        errors.append(GedcomError(ErrorType.error, 'US18', fam, errorMessage))

    return errors