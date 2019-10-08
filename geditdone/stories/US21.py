from geditdone.gedcom_objects import GedcomError

def correct_gender_for_role(parser,db):
    errors = []

    for individual in parser.individuals.values():
        famc = individual.famc
        if famc != None:

            family = parser.families[famc]

            father = family.husband_id
            mother = family.wife_id

            # iterate through all individuals and map family to individuals to check for sex
            for individual2 in parser.individuals.values():

                # if individual is father, check for 'M'
                if individual2.id == father:
                    if individual2.sex == "M":
                        print("GOOD TEST")
                        continue
                    if individual2.sex == "U":
                        print("DO WE NEED THIS CASE?")
                        continue
                    else:
                        errorMessage = f'Husband in {family} does not have the correct gender for role'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US21', family.reference, errorMessage))
                
                # if individual is mother, check for 'F'
                if individual2.id == mother:
                    if individual2.sex == "F":
                        print("GOOD TEST")
                        continue
                    if individual2.sex == "U":
                        print("DO WE NEED THIS CASE?")
                        continue
                    else:
                        errorMessage = f'Wife in {family} does not have the correct gender for role'
                        errors.append(GedcomError(GedcomError.ErrorType.error, 'US21', family.reference, errorMessage))
    
    return errors