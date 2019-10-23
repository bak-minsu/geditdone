from geditdone.gedcom_db import GedcomDatabase
from geditdone.tablehelpers import TableCollector
from prettytable import PrettyTable

def older_siblings_by_age(parser):

    for _, row in GedcomDatabase.families.iterrows():
        famID = row["ID"]
        children = GedcomDatabase.individuals.loc[GedcomDatabase.individuals["famc"] == famID]
        children = children.sort_values(by=["birth"], ascending=True)
        if children.shape[0] > 0:           # if there are more than 0 rows
            TableCollector.add_table(children, "Children in Family {} Descending - Oldest First".format(famID))