from geditdone.error import ErrorCollector, ErrorType

def birth_before_death(parser):
    """Makes sure births are before death"""
    individuals = parser.individuals

    for individual in individuals.values():
        if individual.birth is not None and \
            individual.death is not None and \
            individual.birth >= individual.death:
                errorMessage = f'Birth date {individual.birth} occurs after death date {individual.death}'
                ErrorCollector.add_error(ErrorType.error, 'US03', individual, errorMessage)
        elif individual.birth is None and individual.death is not None:
                errorMessage = f'Birth is null while death date is not.'
                ErrorCollector.add_error(ErrorType.error, 'US03', individual, errorMessage)