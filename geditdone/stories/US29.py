from geditdone.tablecollector import TableCollector

def list_deceased(parser, db):
    errors = []
    individuals = db.individuals
    individuals = individuals.loc[~individuals["death"].isnull()]       # ~ is the loc equivalent of "not"
    TableCollector.add_dataframe(individuals, "Deceased Individuals")
    return errors