from geditdone.gedcom_objects import GedcomError
from datetime import datetime
from dateutil.relativedelta import relativedelta

def birth_before_parent_death(parser):
    """Child should be born before death of mother
    and before 9 months after death of father"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for fam in families.values():
        if fam.child_ids != []:
            for childID in fam.child_ids:
                child = individuals.get(childID)
                if child.birth is not None:
                    if fam.wife_id is not None and \
                        individuals.get(fam.wife_id).death is not None and \
                        individuals.get(fam.wife_id).death <= child.birth:
                            errorMessage = f'Mother {individuals.get(fam.wife_id).name} died before child was born {child.birth}'
                            errors.append(GedcomError(GedcomError.ErrorType.error, 'US09', fam, errorMessage))
                    if fam.husband_id is not None and \
                        individuals.get(fam.husband_id).death is not None:
                            allowableDiff = individuals.get(fam.husband_id).death + relativedelta(months=+9)
                            if allowableDiff <= child.birth:
                                errorMessage = f'Father {individuals.get(fam.husband_id).name} died more than 9 months before child was born {child.birth}'
                                errors.append(GedcomError(GedcomError.ErrorType.error, 'US09', fam, errorMessage))
    return errors