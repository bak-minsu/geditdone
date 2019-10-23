from geditdone.error import GedcomError, ErrorType

def no_marriages_to_children(parser, db):
    errors = []

    for individual in parser.individuals.values():
        famc = individual.famc
        if famc != None:
            family = parser.families[famc]
            mother = family.wife_id
            father = family.husband_id
            myself = individual.id
            married_to_parent = db.families.loc[
                (db.families["wife_id"] == mother) & (db.families["husband_id"] == myself) |
                (db.families["wife_id"] == myself) & (db.families["husband_id"] == father) 
                ]
            for family in married_to_parent.iterrows():
                family = family[1]
                parent = ""
                if myself == family.husband_id:
                    parent = family.wife_id
                else: parent = family.husband_id
                errorMessage = f'Parent {parent} married child {myself}'
                errors.append(GedcomError(ErrorType.error, 'US17', family.reference, errorMessage))
    return errors