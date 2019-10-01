from geditdone.gedcom_objects import GedcomError

def birth_before_death(parser):
    """Makes sure births are before death"""
    individuals = parser.individuals
    errors = []

    for individual in individuals.values():
        if individual.birth is not None and \
            individual.death is not None and \
            individual.birth >= individual.death:
                errorMessage = f'Individual {individual.id} birth date {individual.birth} occurs after death date {individual.death}'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US03', None, errorMessage))
        elif individual.birth is None and individual.death is not None:
                errorMessage = f'Individual {individual.id} birth is null while death date is not.'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US03', None, errorMessage))
    
    return errors