def less_than_150_years_old(parser):
    """Makes sure nobody reaches 150 years old"""
    individuals = parser.individuals
    for individual in individuals.values():
        # birth true, death true, less than 150
        if individual.birth is not None and \
            individual.death is not None and \
            individual.death.yearInt-individual.birth.yearInt >= 150:
            return False
        # birth true, death false, less than 150
        else if individual.birth is not None and \
            individual.death is None and \
            individual.death.yearInt-individual.birth.yearInt >= 150:
            return False
    return True
