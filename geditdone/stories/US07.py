from datetime import datetime

def less_than_150_years_old(parser):
    """Makes sure nobody reaches 150 years old"""
    individuals = parser.individuals
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
                if (individual_death_year-individual_birth_year >= 150):
                    return False
            # if death is not true (still alive)
            else:
                current_date_year=datetime.today().year
                # print("current_date_year: ",current_date_year)
                if (current_date_year-individual_birth_year >= 150):
                    return False
    return True
