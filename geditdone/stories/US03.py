def birth_before_death(parser):
    """Makes sure births are before death"""
    individuals = parser.individuals
    for individual in individuals.values():
        if individual.death is not None and \
            individual.birth >= individual.death:
            return False
        elif individual.birth is None and individual.death is not None:
            return False
    return True
