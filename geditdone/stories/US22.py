from geditdone.error import ErrorCollector, ErrorType

def unique_ids(parser):
    errors = []

    for individual in parser.individuals.values():
        pass

    for family in parser.families.values():
        pass
        #errors.append(GedcomError(ErrorType.error, 'US21', family, errorMessage))

    return errors