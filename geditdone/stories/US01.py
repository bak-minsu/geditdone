from datetime import datetime

def dates_before_current_date(parser):
    """Makes sure all dates are before current date"""
    individuals = parser.individuals
    families = parser.families

    current_date = datetime.today()

    # check all individual dates: birth, death
    for individual in individuals.values():
        if individual.birth is not None and individual.death is not None:
            if individual.birth >= current_date or \
                individual.death >= current_date:
                return False

    # check all family dates: marriage, divorce
    for family in families.values():
        if family.married is not None and family.divorced is not None:
            if family.married >= current_date or \
                family.divorced >= current_date:
                return False

    return True
