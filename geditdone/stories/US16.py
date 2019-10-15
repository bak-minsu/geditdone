from geditdone.gedcom_objects import GedcomError

def male_last_name(parser, db):
    errors = []

    for family in parser.families.values():
        father = family.husband_id
        children = family.child_ids

        # DEBUG
        #print()
        #print("father id is: ", father)
        #print("children ids are: ", children)
        #print()

        # obtain father last_name 
        for individual in parser.individuals.values():
            if individual.id == father:
                father_last_name=individual.name.split()[1]
        #print("father_last_name: ", father_last_name)

        child_last_name = ""

        for individual in parser.individuals.values():
            #print("-----")
            #print("individual is is: ", individual.name)
            for i in range(len(children)):
                if individual.sex == "M":
                    if individual.id == children[i]:
                        child_last_name = individual.name.split()[1]
                        #print("child_last_name is: ", child_last_name)
                        if child_last_name != father_last_name:
                            errorMessage = f'Males ({individual.name}) in {family} do not have the same last name'
                            errors.append(GedcomError(GedcomError.ErrorType.error, 'US16', family, errorMessage))
                #elif individual.sex == "F" and individual.id == children[i]:
                    #print("child is female")

    return errors