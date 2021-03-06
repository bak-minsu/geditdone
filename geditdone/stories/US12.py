from geditdone.error_objects import GedcomError, ErrorType
from datetime import datetime

def parents_not_too_old(parser):
    """Mother should be less than 60 years older than her children
    and father should be less than 80 years older than his children"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for fam in families.values():
        if fam.child_ids != []:
            for childID in fam.child_ids:
                child = individuals.get(childID)
                if child.birth is not None:
                    childBirthYear = (datetime.strptime(str(child.birth), '%Y-%m-%d')).year
                    if fam.wife_id is not None and \
                        individuals.get(fam.wife_id).birth is not None:
                            momBirthYear = (datetime.strptime(str(individuals.get(fam.wife_id).birth), '%Y-%m-%d')).year
                            if childBirthYear - momBirthYear >= 60:
                                errorMessage = f'Mother {individuals.get(fam.wife_id).name} born {momBirthYear}, 60+ years before child was born {child.birth}'
                                errors.append(GedcomError(ErrorType.error, 'US12', fam, errorMessage))
                    if fam.husband_id is not None and \
                        individuals.get(fam.husband_id).birth is not None:
                            dadBirthYear = (datetime.strptime(str(individuals.get(fam.husband_id).birth), '%Y-%m-%d')).year
                            if childBirthYear - dadBirthYear >= 80:
                                errorMessage = f'Father {individuals.get(fam.husband_id).name} born {dadBirthYear}, 80+ years before child was born {child.birth}'
                                errors.append(GedcomError(ErrorType.error, 'US12', fam, errorMessage))
    return errors