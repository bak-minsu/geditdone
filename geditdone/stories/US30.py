from geditdone.tablehelpers import TableHelpers
from geditdone.error_objects import GedcomError, ErrorType

def list_living_married(parser, db):
    tables = []
    individuals = db.individuals
    #individuals = individuals.loc[individuals["death"].isnull()]

    individuals = parser.individuals
    families = parser.families
    errors = []
    married_individuals = []

    for fam in families.values():
        if fam.married:
            for individual in individuals.values():
                if (individual.id == individuals.get(fam.wife_id) or individual.id == individuals.get(fam.husband_id)):
                    married_individuals.append(individual.name)
    #return(married_individuals)

    pt = TableHelpers.dataframe2table(married_individuals, "Living Married Individuals")
    tables.append(pt)
    return tables