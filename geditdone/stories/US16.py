from geditdone.error import ErrorCollector, ErrorType

def male_last_name(parser):

    for family in parser.families.values():
        father = family.husband_id
        children = family.child_ids

        # obtain father last_name 
        for individual in parser.individuals.values():
            if individual.id == father:
                father_last_name=individual.name.split()[1]

        child_last_name = ""

        for individual in parser.individuals.values():
            for i in range(len(children)):
                if individual.sex == "M":
                    if individual.id == children[i]:
                        child_last_name = individual.name.split()[1]
                        if child_last_name != father_last_name:
                            errorMessage = f'Males ({individual.name}) in {family} do not have the same last name'
                            ErrorCollector.add_error(ErrorType.error, 'US16', family, errorMessage)
