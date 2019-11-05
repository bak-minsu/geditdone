from geditdone.tablehelpers import TableHelpers

def older_siblings_by_age(parser, db):
    tables = []
    for _, row in db.families.iterrows():
        famID = row["ID"]
        children = db.individuals.loc[db.individuals["famc"] == famID]
        children = children.sort_values(by=["birth"], ascending=True)   # Ascending birth dates
        if children.shape[0] > 0:                                       # if there are more than 0 rows
            pt = TableHelpers.dataframe2table(children, "US28 - Children in Family {} Descending - Oldest First".format(famID))
            tables.append(pt)
    return tables