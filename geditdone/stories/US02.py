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
                    errorMessage = f'{individual.id}\'s birth date {individual.birth} occurs after marriage date {family.married}'
                    errors.append(GedcomError(GedcomError.ErrorType.error, 'US02', family.id, errorMessage))
            elif individual.birth is None and family.married is not None:
                # TODO talk about this logic, not sure it makes sense
                    errorMessage = f'{individual.id}\'s does not have a birth date before marriage date {family.married}'
                    errors.append(GedcomError(GedcomError.ErrorType.error, 'US02', family.id, errorMessage))

    return errors
