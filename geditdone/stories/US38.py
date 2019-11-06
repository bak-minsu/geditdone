from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

def upcoming_birthdays(parser):
    tables = []
    today = date.today()
    upcoming_people = []
    for individual in parser.individuals.values():
        updated = date(today.year, individual.birth.month, individual.birth.day)
        # If we've passed the date, we check the next year
        if updated < today:
            updated = date(today.year+1, individual.birth.month, individual.birth.day)
        if DateHelpers.date_diff(updated, today, "days") <= 30:
            upcoming_people.append(individual)
    tables.append(TableHelpers.individuals2table(upcoming_people, "US38: Upcoming Birthdays"))
    return tables