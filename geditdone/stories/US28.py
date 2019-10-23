from geditdone.tablecollector import TableCollector
from prettytable import PrettyTable

def older_siblings_by_age(parser, db):
    errors = []
    for _, row in db.families.iterrows():
        famID = row["ID"]
        children = db.individuals.loc[db.individuals["famc"] == famID]
        children = children.sort_values(by=["birth"], ascending=True)   # Ascending birth dates
        if children.shape[0] > 0:                                       # if there are more than 0 rows
            TableCollector.add_dataframe(children, "Children in Family {} Descending - Oldest First".format(famID))
    return errors