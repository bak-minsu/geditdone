from geditdone.error_objects import GedcomError, ErrorType

def unique_names_and_birth_date(parser):
    """Returns errors for individuals sharing a name and a birth date"""
    individuals = parser.individuals
    errors = []

    indivs_by_name_birthdate = {}
    for indi in individuals.values():
        # If name or birth are not given for the individual, these keys will be None
        # This means two people with the same name and no birthday will give a warning
        name_birthdate = (indi.name, indi.birth)
        if name_birthdate in indivs_by_name_birthdate:
            other_indi = indivs_by_name_birthdate[name_birthdate]
            errorMessage = f'Individual {indi} has the same name and birth date as {other_indi}'
            errors.append(GedcomError(ErrorType.anomaly, 'US23', indi, errorMessage))
        else:
            indivs_by_name_birthdate[name_birthdate] = indi

    return errors