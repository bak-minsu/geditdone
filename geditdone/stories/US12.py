from geditdone.gedcom_objects import GedcomError

def parents_not_too_old(parser):
    """Makes sure birth happens before parent death"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    # TODO actually implement
    for fam in families.values():
        if fam.child_ids != []:
            for childID in fam.child_ids:
                child = individuals.get(childID)
                if child.birth is not None and \
                    fam.married is not None and \
                    child.birth <= fam.married:
                        errorMessage = f'Married {fam.married} after child was born {child.birth}'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US08', fam, errorMessage))
                # elif child.birth is None and \
                #     fam.married is not None:
                #         errorMessage = f'Family {fam.id} is married but has a child with a null birth date'
                #         errors.append(GedcomError(GedcomError.ErrorType.error, 'US08', fam, errorMessage))
    return errors