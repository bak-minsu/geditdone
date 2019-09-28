def divorce_before_death(parser):
    """Makes sure divorces occur before death"""
    individuals = parser.individuals
    families = parser.families
    for individual in individuals.values():
        for family in families.values():
            if family.divorced is not None and \
                individual.death is not None and \
                family.divorced >= individual.death:
                return False
    return True
