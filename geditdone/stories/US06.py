from geditdone.gedcom_objects import GedcomError

def divorce_before_death(parser):
    """Makes sure divorces come before death"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for individual in individuals.values():
        if individual.fams is not None:
            fam = families.get(individual.fams)
            if fam is not None:
                if fam.divorced is not None and \
                    individual.death is not None and \
                    fam.divorced >= individual.death:
                        errorMessage = f''
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US06', individual, "Divorce after death"))
                elif fam.divorced is None and \
                    individual.death is not None:
                        errorMessage = f''
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US06', individual, "Divorce after death"))

    return errors
