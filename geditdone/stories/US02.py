from geditdone.gedcom_objects import GedcomError

def birth_before_marriage(parser):
    """Makes sure births are before marriage"""
    families = parser.families
    individuals = parser.individuals
    errors = []

    for individual in individuals.values():
        for family in families.values():
            if individual.birth is not None and \
                family.married is not None and \
                individual.birth >= family.married:
                    errorMessage = f'Birth date {individual.birth} occurs after marriage date {family.married}'
                    errors.append(GedcomError(GedcomError.ErrorType.error, 'US02', family, errorMessage))
            # elif individual.birth is None and family.married is not None:
            #     # TODO talk about this logic, not sure it makes sense
            #     errorMessage = f'Does not have a birth date before marriage date {family.married}'
            #     errors.append(GedcomError(GedcomError.ErrorType.error, 'US02', family, errorMessage))

    return errors
