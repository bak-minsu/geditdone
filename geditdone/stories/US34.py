from geditdone.tablehelpers import TableHelpers
from datetime import datetime
from prettytable import PrettyTable
from geditdone.datehelpers import DateHelpers

# List all couples who were married when the older spouse was more than twice as old as the younger spouse
def list_large_age_differences(parser, db):

    list_tables = []

    my_table = PrettyTable()
    my_table.title = "US34: List Large Age Differences"
    my_table.field_names = ["id", "name", "sex", "birth", "marriage", "age_married", "death", "famc","fams"]

    lower_age = 0
    higher_age = 0

    for fam in parser.families.values():

        spouse1=[]
        spouse2=[]

        for spouse in parser.individuals.values():
            if (spouse.id == fam.wife_id) or (spouse.id == fam.husband_id):
                spouse_age = DateHelpers.date_diff(spouse.birth, fam.married,'years')

                if len(spouse1)==0:
                    spouse1.extend([spouse.id, spouse.name, spouse.sex, spouse.birth, fam.married, round(spouse_age,1), spouse.death, spouse.famc, spouse.fams])
                else:
                    spouse2.extend([spouse.id, spouse.name, spouse.sex, spouse.birth, fam.married, round(spouse_age,1), spouse.death, spouse.famc, spouse.fams])

                if lower_age==0 and higher_age==0:
                    lower_age = spouse_age
                else:
                    if spouse_age>lower_age:
                        higher_age = spouse_age
                    elif spouse_age<lower_age:
                        higher_age = lower_age
                        lower_age = spouse_age

        if higher_age/2 > lower_age:
            my_table.add_row(spouse1)
            my_table.add_row(spouse2)

    list_tables.append(my_table)

    return list_tables