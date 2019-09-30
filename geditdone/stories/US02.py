def birth_before_marriage(parser):
    """Makes sure births are before marriage"""
    families = parser.families
    individuals = parser.individuals
    for individual in individuals.values():
        for family in families.values():
            if individual.birth is not None and \
                family.married is not None and \
                individual.birth >= family.married:
                return False
            elif individual.birth is None and family.married is not None:
                return False
    return True
