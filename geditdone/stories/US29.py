from geditdone.tablehelpers import TableHelpers
from datetime import date

def list_deceased(parser, db):
    tables = []
    today = date.today()
    individuals = db.individuals
    individuals = individuals.loc[(~individuals["death"].isnull())] # ~ is the loc equivalent of "not"
    pt = TableHelpers.dataframe2table(individuals, "US29 - Deceased Individuals")
    tables.append(pt)
    return tables