from geditdone.gedcom_db import GedcomDatabase
from geditdone.gedcom_objects import GedcomError

def no_marriages_to_children(parser):
    errors = []

    for individual in parser.individuals.values():
        famc = individual.famc
        if famc != None:
            family = parser.families[famc]
            mother = family.wife_id
            father = family.husband_id
            myself = individual.id
            fam_df = GedcomDatabase.families
            married_to_parent = fam_df.loc[
                (fam_df["wife_id"] == mother) & (fam_df["husband_id"] == myself) |
                (fam_df["wife_id"] == myself) & (fam_df["husband_id"] == father) 
                ]
            for family in married_to_parent.iterrows():
                family = family[1]
                parent = ""
                if myself == family.husband_id:
                    parent = family.wife_id
                else: parent = family.husband_id
                errorMessage = f'Parent {parent} married child {myself}'
                errors.append(GedcomError(GedcomError.ErrorType.error, 'US17', family.reference, errorMessage))
    return errors