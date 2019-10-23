from geditdone.gedcom_db import GedcomDatabase
from geditdone.gedcom_objects import GedcomError
from geditdone.tablehelpers import TableHelpers

def list_deceased(parser):
    errors = []
    individuals = GedcomDatabase.individuals
    individuals = individuals.loc[~individuals["death"].isnull()]
    TableHelpers.print_table(individuals, "Deceased Individuals")
    return errors