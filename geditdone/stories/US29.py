from geditdone.tablehelpers import TableHelpers

def list_deceased(parser, db):
    tables = []
    individuals = db.individuals
    individuals = individuals.loc[~individuals["death"].isnull()]       # ~ is the loc equivalent of "not"
    pt = TableHelpers.dataframe2table(individuals, "Deceased Individuals")
    tables.append(pt)
    return tables