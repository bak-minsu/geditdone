from datetime import date
from dateutil.relativedelta import relativedelta
from geditdone.datehelpers import DateHelpers
from geditdone.tablehelpers import TableHelpers
import pandas as pd

'''
Include person's current age when listing individuals
'''
def list_ages(parser, db):
    tables = []
    ages = []
    for indiv in parser.individuals.values():
        if indiv.birth is not None:
            ages.append(DateHelpers.calculate_age(indiv.birth, None))
        else:
            ages.append(None)
    individuals = db.individuals
    individuals["Age"] = pd.Series(ages).values
    newTable = TableHelpers.dataframe2table(individuals, "US27: Individuals and Ages")
    tables.append(newTable)
    return tables
