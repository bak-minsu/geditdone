from geditdone.tablehelpers import TableHelpers
from datetime import datetime
#from dateutil.relativedelta import relativedelta

# over 30 and never married
def list_living_single(parser, db):
    tables = []
    #individuals = db.individuals
    individuals = parser.individuals

    single_individuals = []


    for individual in individuals:
        individual_birth_year=(datetime.strptime(str(individual.birth), '%Y-%m-%d')).year
        individual_death_year=(datetime.strptime(str(individual.death), '%Y-%m-%d')).year
        age = individual_death_year-individual_birth_year
        if (age >= 30):
            # if no spouse found, add name to list of names
            if individual.fams is None:
                single_individuals.append(individual.name)

    pt = TableHelpers.dataframe2table(single_individuals, "Living Single Individuals")
    tables.append(pt)
    return tables
