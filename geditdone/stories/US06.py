def divorce_before_death(parser):
    """Makes sure divorces come before death"""
    individuals = parser.individuals
    families = parser.families
    for individual in individuals.values():
        if individual.fams is not None:
            fam = families.get(individual.fams)
            if fam.divorced is not None and \
                individual.death is not None and \
                fam.divorced >= individual.death:
                    return False
            elif fam.divorced is None and \
                individual.death is not None:
                    return False
    return True
