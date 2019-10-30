from geditdone.tablehelpers import TableHelpers
from geditdone.error_objects import GedcomError, ErrorType
from prettytable import PrettyTable


def list_living_married(parser, db):

    my_table = PrettyTable()
    my_table.field_names = ["id", "name", "sex", "birth", "death", "famc","fams"]

    for person in parser.individuals.values():
        if ((person.fams is not None) and (person.death is None)):
            my_table.add_row([person.id, person.name, person.sex, person.birth, person.death, person.famc, person.fams])
    return my_table