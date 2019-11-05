from datetime import datetime
from geditdone.tablehelpers import TableHelpers
from prettytable import PrettyTable
from geditdone.datehelpers import DateHelpers
from geditdone.error_objects import GedcomError, ErrorType


def reject_illegitimate_dates(parser):

    # verify date
    def date_verifier(date_to_check):

        # check leap year
        def is_leap_year(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            if year % 4 == 0:
                return True
            else:
                return False

        # return out if year is negative 
        if str(date_to_check)[:1]=='-':
            return False

        # slit year/month/day, need to use this to bypass datetime inherit checks
        dt=str(date_to_check).split('-')

        # check negatives, days greater than 31
        if int(dt[2])>31 or int(dt[1])>12 or int(dt[2])<1 or int(dt[1])<1 or int(dt[0])<0:
            return False

        # first 7 months, odd months have 31 days
        if int(dt[1])<=7:
            if int(dt[1])%2==0:
                # check leap years, days for Feb
                if int(dt[1])==2:
                    if is_leap_year(int(dt[0])):
                        if int(dt[2])>29:
                            return False
                    elif int(dt[2])>28:
                            return False
                if int(dt[2])>30:
                    return False
        # last 5 months, odd months have 30 days
        elif int(dt[1])>=8:
            if int(dt[1])%2==1:
                if int(dt[2])>30:
                    return False

        return True

    errors = []
    #print()
    valid_date = True

    # check all individual dates: birth, death
    for individual in parser.individuals.values():
        if  individual.birth is not None:
            valid_date = date_verifier(individual.birth)

            if valid_date==False:
                errorMessage = f'Birth date {individual.birth} for {individual.name} is invalid'
                #print(errorMessage)
                errors.append(GedcomError(ErrorType.error, 'US42', individual, errorMessage))
            #else:
            #    print(f'Birth date {individual.birth} for {individual.name} is valid')

        if individual.death is not None:
            valid_date = date_verifier(individual.death)

            if valid_date==False:
                errorMessage = f'Death date {individual.death} for {individual.name} is invalid'
                #print(errorMessage)
                errors.append(GedcomError(ErrorType.error, 'US42', individual, errorMessage))
            #else:
            #    print(f'Death date {individual.death} for {individual.name} is valid')

    # check all family dates: marriage, divorce
    for family in parser.families.values():
        if family.married is not None:
            valid_date = date_verifier(family.married)

            if valid_date==False:
                errorMessage = f'Marriage date {family.married} for family {family.id} is invalid'
                #print(errorMessage)
                errors.append(GedcomError(ErrorType.error, 'US42', family, errorMessage))
            #else:
            #    print(f'Marriage date {family.married} for family {family.id} is valid')

        if family.divorced is not None:
            valid_date = date_verifier(family.divorced)

            if valid_date==False:
                errorMessage = f'Divorce date {family.divorced} for family {family.id} is invalid'
                #print(errorMessage)
                errors.append(GedcomError(ErrorType.error, 'US42', family, errorMessage))
            #else:
            #    print(f'Divorced date {family.divorced} for family {family.id} is valid')

    return errors