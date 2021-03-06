from geditdone.error_objects import GedcomError, ErrorType

def divorce_before_death(parser):
    """Makes sure divorces come before death"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for individual in individuals.values():
        if individual.fams is not None:
            fam = families.get(individual.fams)
            # print(individual.name)
            # print(individual.death)
            # print(fam.divorced)
            if fam is not None:
                if fam.divorced is not None and \
                    individual.death is not None and \
                    fam.divorced >= individual.death:
                        errorMessage = f'Divorced {fam.divorced} after death {individual.death}'
                        errors.append(GedcomError(ErrorType.error, 'US06', individual, errorMessage))
                # elif fam.divorced is None and \
                #     individual.death is not None:
                #         errorMessage = f''
                #         errors.append(GedcomError(ErrorType.error, 'US06', individual, errorMessage))

    return errors
