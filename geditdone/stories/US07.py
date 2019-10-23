from geditdone.error_objects import GedcomError, ErrorType
from datetime import datetime

def less_than_150_years_old(parser):
    """Makes sure nobody reaches 150 years old"""
    individuals = parser.individuals
    errors = []

    for individual in individuals.values():
        # print("---------------------------------------------------------")
        # if birth is true
        if individual.birth is not None:
            individual_birth_year=(datetime.strptime(str(individual.birth), '%Y-%m-%d')).year
            # print("individual_birth_year: ",individual_birth_year)
            # if death is true (dead)
            if individual.death is not None:
                individual_death_year=(datetime.strptime(str(individual.death), '%Y-%m-%d')).year
                # print("individual_death_year: ",individual_death_year)
                age = individual_death_year-individual_birth_year
                if (age >= 150):
                    errorMessage = f'The person is more than 150 years old, at {age} years old'
                    errors.append(GedcomError(ErrorType.error, 'US07', individual, errorMessage))
            # if death is not true (still alive)
            else:
                current_date_year=datetime.today().year
                # print("current_date_year: ",current_date_year)
                age = current_date_year-individual_birth_year
                if (age >= 150):
                    errorMessage = f'The person is more than 150 years old, at {age} years old'
                    errors.append(GedcomError(ErrorType.error, 'US07', individual, errorMessage))

    return errors
