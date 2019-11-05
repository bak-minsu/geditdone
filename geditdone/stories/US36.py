from geditdone.tablehelpers import TableHelpers
from geditdone.error_objects import GedcomError, ErrorType
from prettytable import PrettyTable


def list_recent_deaths(parser, db):
    tables = []

    my_table = PrettyTable()
    my_table.title = "US36: Recent Deaths"
    my_table.field_names = ["id", "name", "sex", "birth", "death", "famc","fams"]

    for person in parser.individuals.values():
        pass

    tables.append(my_table)

    return tables