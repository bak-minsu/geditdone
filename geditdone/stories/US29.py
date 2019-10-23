from geditdone.gedcom_db import GedcomDatabase
from geditdone.tablecollector import TableCollector

def list_deceased(parser):
    individuals = GedcomDatabase.individuals
    individuals = individuals.loc[~individuals["death"].isnull()]       # ~ is the loc equivalent of "not"
    TableCollector.add_dataframe(individuals, "Deceased Individuals")