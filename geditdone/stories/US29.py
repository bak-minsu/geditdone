from geditdone.gedcom_db import GedcomDatabase
from geditdone.tablecollector import TableCollector

def list_deceased(parser):
    individuals = GedcomDatabase.individuals
    individuals = individuals.loc[~individuals["death"].isnull()]
    TableCollector.add_table(individuals, "Deceased Individuals")