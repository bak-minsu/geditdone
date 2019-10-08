from geditdone.gedcom_objects import GedcomError

def male_last_name(parser, db):
    errors = []

    # check individual and son have same last name 
    for individual in parser.individuals.values():
        famc = individual.famc
        if famc != None:

            family = parser.families[famc]
            father = family.husband_id
            myself = individual.id

            # get individual's father's full_name from ID
            for individual2 in parser.individuals.values():
                if individual2.id == father:
                    fatherfather_full_name = individual2.name

            # get individual's full_name
            myself_full_name = individual.name

            # get last_name from full_name
            father_last_name = " ".join(father_full_name.split()[1:-1])
            myself_last_name = " ".join(myself_full_name.split()[1:-1])

            # debug statements
            print("myself_last_name: ", myself_last_name)
            print("father_last_name:", father_last_name)


            # error out if last_name does not match
            if father_last_name != myself_last_name:
                errorMessage = f'Males in {family} do not have the same last name'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US16', family.reference, errorMessage))

    return errors