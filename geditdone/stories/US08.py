from geditdone.gedcom_objects import GedcomError

def birth_before_parent_marriage(parser):
    """Makes sure birth happens after parent marriage"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for fam in families.values():
        if fam.child_ids != []:
            for childID in fam.child_ids:
                child = individuals.get(childID)
                if child.birth is not None and \
                    fam.married is not None and \
                    child.birth <= fam.married:
                        errorMessage = f'Married {fam.married} after child was born {child.birth}'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US08', fam, errorMessage))
                if child.birth is not None and \
                    fam.divorced is not None:
                        # TODO see US09 as well
                        allowableDiff = fam.divorced # + 9 months
                        if allowableDiff <= child.birth:
                            errorMessage = f'Divorced {fam.divorced} more than 9 months before child was born {child.birth}'
                            errors.append(GedcomError(GedcomError.ErrorType.error, 'US08', fam, errorMessage))
                # elif child.birth is None and \
                #     fam.married is not None:
                #         errorMessage = f'Family {fam.id} is married but has a child with a null birth date'
                #         errors.append(GedcomError(GedcomError.ErrorType.error, 'US08', fam, errorMessage))
    return errors