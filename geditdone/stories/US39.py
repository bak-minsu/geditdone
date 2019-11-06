from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

def upcoming_anniversaries(parser):
    tables = []
    today = date.today()
    upcoming_people = []
    found = False
    for family in parser.families.values():
        updated = date(today.year, family.married.month, family.married.day)
        # If we've passed the date, we check the next year
        if updated < today:
            updated = date(today.year, family.married.month, family.married.day)
        if DateHelpers.date_diff(updated, today, "days") <= 30:
            if not found: found = True
            upcoming_people.append(family)
    if found:
        tables.append(TableHelpers.families2table(upcoming_people, "US39: Upcoming Anniversaries"))
    return tables