from geditdone.gedcom_objects import GedcomError

def birth_before_death(parser):
    """Makes sure births are before death"""
    individuals = parser.individuals
    errors = []

    for individual in individuals.values():
        if individual.birth is not None and \
            individual.death is not None and \
            individual.birth >= individual.death:
                errorMessage = f''
                errors.append(GedcomError.ErrorType.error, 'US0X', None, errorMessage)
        elif individual.birth is None and individual.death is not None:
                errorMessage = f''
                errors.append(GedcomError.ErrorType.error, 'US0X', None, errorMessage)
    
    return errors