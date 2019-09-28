def marriage_before_death(parser):
    """Makes sure marriages come before death"""
    individuals = parser.individuals
    families = parser.families
    for individual in individuals.values():
        for family in families.values():
            if family.married is not None and \
                individual.death is not None and \
                family.married >= individual.death:
                return False
    return True
