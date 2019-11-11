from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

'''
List all people in a GEDCOM file who were born in the last 30 days
'''
def list_recent_births(parser, db):
    tables = []
    recents = []
    today = date.today()

    for person in parser.individuals.values():
        if person.birth is not None:
            if (DateHelpers.dates_within(today, person.birth, 30, "days")):
                recents.append(person)

    tables.append(TableHelpers.individuals2table(recents, "US35: Recent Births"))

    return tables