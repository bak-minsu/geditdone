from geditdone.error_objects import GedcomError, ErrorType

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
                        errorMessage = f'Married {fam.married} after death {individual.death}'
                        errors.append(GedcomError(ErrorType.error, 'US05', individual, errorMessage))
                # elif fam.married is None and \
                #     individual.death is not None:
                #         errorMessage = f'Not married but has died'
                #         errors.append(GedcomError(ErrorType.error, 'US08', fam, errorMessage))
    return errors