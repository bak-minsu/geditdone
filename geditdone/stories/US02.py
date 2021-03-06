from geditdone.error_objects import GedcomError, ErrorType

def birth_before_marriage(parser):
    """Makes sure births are after marriage"""
    families = parser.families
    individuals = parser.individuals
    errors = []

    for individual in individuals.values():
        if individual.famc != None:
            fam = families.get(individual.famc)
            if individual.birth is not None and \
                fam.married is not None and \
                individual.birth <= fam.married:
                    errorMessage = f'Birth date {individual.birth} occurs before marriage date {fam.married}'
                    errors.append(GedcomError(ErrorType.error, 'US02', fam, errorMessage))

    return errors
