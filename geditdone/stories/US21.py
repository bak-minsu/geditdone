from geditdone.error import ErrorCollector, ErrorType

def correct_gender_for_role(parser):
    for family in parser.families.values():
        father = family.husband_id
        mother = family.wife_id

        for individual in parser.individuals.values():
            if individual.id == father:
                #if individual.sex == "M":
                #    print("FATHER IDENTIFIED AND CONFIRMED")
                if individual.sex =="U":
                     errorMessage = f'Husband in {family} does not have the correct gender for role, has {individual.sex} instead.'
                     ErrorCollector.add_error(ErrorType.error, 'US21', family, errorMessage)
                elif individual.sex != "M":
                     errorMessage = f'Husband in {family} does not have the correct gender for role, has {individual.sex} instead.'
                     ErrorCollector.add_error(ErrorType.error, 'US21', family, errorMessage) 
            elif individual.id == mother:
                #if individual.sex == "F":
                #    print("MOTHER IDENTIFIED AND CONFIRMED")
                if individual.sex =="U":
                     errorMessage = f'Wife in {family} does not have the correct gender for role, has {individual.sex} instead.'
                     ErrorCollector.add_error(ErrorType.error, 'US21', family, errorMessage)
                elif individual.sex != "F":
                     errorMessage = f'Wife in {family} does not have the correct gender for role, has {individual.sex} instead.'
                     ErrorCollector.add_error(ErrorType.error, 'US21', family, errorMessage)
