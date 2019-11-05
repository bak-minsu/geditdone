from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

def upcoming_birthdays(parser):
    tables = []
    today = date.today()
    upcoming_people = []
    found = False
    for individual in parser.individuals.values():
        updated = DateHelpers.change_year(individual.birth, today.year)
        # If we've passed the date, we check the next year
        if updated < today:
            updated = DateHelpers.change_year(individual.birth, today.year+1)
        if DateHelpers.date_diff(updated, today, "days") <= 30:
            if not found: found = True
            upcoming_people.append(individual)
    if found:
        tables.append(TableHelpers.individuals2table(upcoming_people, "US38 - Upcoming Birthdays"))
    return tables