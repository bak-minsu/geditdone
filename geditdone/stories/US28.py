from geditdone.gedcom_db import GedcomDatabase
from geditdone.gedcom_objects import GedcomError
from geditdone.tablehelpers import TableHelpers
from prettytable import PrettyTable

def older_siblings_by_age(parser):
    errors = []

    def get_all_children(famID):
        """Gets all children in increasing birth order"""
        children = GedcomDatabase.individuals.loc[GedcomDatabase.individuals["famc"] == famID]
        children = children.sort_values(by=["birth"], ascending=True)
        return children

    for _, row in GedcomDatabase.families.iterrows():
        famID = row["ID"]
        children = get_all_children(famID)
        if children.shape[0] > 0:           # if there are more than 0 rows
            TableHelpers.print_table(children, "Family ID: {}".format(famID))
            
    return errors