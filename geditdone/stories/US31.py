from geditdone.tablehelpers import TableHelpers
from datetime import datetime

# over 30 and never married
def list_living_single(parser, db):
    tables = []
    individuals = db.individuals

    single_individuals = []

    for individual in individuals:
        individual_birth_year=(datetime.strptime(str(individual.birth), '%Y-%m-%d')).year
        individual_death_year=(datetime.strptime(str(individual.death), '%Y-%m-%d')).year
        age = individual_death_year-individual_birth_year
        if (age >= 30):
            single_individuals.append(individual.name)

    pt = TableHelpers.dataframe2table(single_individuals, "Living Single Individuals")
    tables.append(pt)
    return tables
