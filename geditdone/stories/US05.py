from geditdone.gedcom_objects import GedcomError

def marriage_before_death(parser):
    """Makes sure mariages come before death"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for individual in individuals.values():
        if individual.fams is not None:
            fam = families.get(individual.fams)
            if fam is not None:
                if fam.married is not None and \
                    individual.death is not None and \
                    fam.married >= individual.death:
                        errorMessage = f'Individual {individual.id} was married {fam.married} after death {individual.death}'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US05', None, errorMessage))
    return errors