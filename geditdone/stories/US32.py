from geditdone.tablehelpers import TableHelpers
from pandas import DataFrame

def list_multiple_births(parser, db):
    tables = []
    multiple_birth_children = db.individuals.groupby(['famc','birth'])
    multiple_births = DataFrame({'Children': multiple_birth_children.size()}).reset_index()
    multiple_births = multiple_births[(multiple_births.Children > 1)].rename(columns={'famc':'FamID','birth':'Birthdate'})
    pt = TableHelpers.dataframe2table(multiple_births, "US32: Multiple Births")
    tables.append(pt)
    return tables