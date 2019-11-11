from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

'''
List all people in a GEDCOM file who died in the last 30 days
'''
def list_recent_deaths(parser, db):
    tables = []
    recents = []
    today = date.today()

    for person in parser.individuals.values():
        if person.death is not None:
            if (DateHelpers.dates_within(today, person.death, 30, "days")):
                recents.append(person)

    tables.append(TableHelpers.individuals2table(recents, "US36: Recent Deaths"))

    return tables