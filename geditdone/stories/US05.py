def marriage_before_death(parser):
    """Makes sure marriages come before death"""
    individuals = parser.individuals
    families = parser.families
    for individual in individuals.values():
        if individual.fams is not None:
            fam = families.get(individual.fams)
            if fam.married is not None and \
                individual.death is not None and \
                fam.married >= individual.death:
                    return False
            elif fam.married is None and \
                individual.death is not None:
                    return False
    return True