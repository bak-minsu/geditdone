from geditdone.tablehelpers import TableHelpers
from datetime import datetime
from prettytable import PrettyTable
from geditdone.datehelpers import DateHelpers
#from dateutil.relativedelta import relativedelta

# over 30 and never married
def list_living_single(parser, db):

    tables = []

    my_table = PrettyTable()
    my_table.title = "US31: List Living Single"
    my_table.field_names = ["id", "name", "sex", "birth", "death", "famc","fams"]

    for person in parser.individuals.values():

        age = DateHelpers.calculate_age(person.birth, None)

        if ((person.fams is None) and (person.death is None) and (age >= 30)):
            my_table.add_row([person.id, person.name, person.sex, person.birth, person.death, person.famc, person.fams])

    tables.append(my_table)

    return tables