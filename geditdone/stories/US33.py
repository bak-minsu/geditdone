from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers

def list_orphans(parser):
    '''List all children younger than 18 with both parents deceased'''
    tables = []
    orphans = []
    for id in parser.families:
        family = parser.families[id]
        mother = parser.individuals[family.wife_id]
        father = parser.individuals[family.husband_id]
        if mother.death and father.death:
            for child_id in family.child_ids:
                child = parser.individuals[child_id]
                if DateHelpers.calculate_age(child.birth, None) < 18:
                    orphans.append(child)
    pt = TableHelpers.individuals2table(orphans, "US33: List Orphans")
    tables.append(pt)
    return tables