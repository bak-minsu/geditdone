from geditdone.gedcom_objects import GedcomError
from geditdone.datehelpers import datehelpers
from datetime import date
from functools import reduce

def sibling_spacing(parser):
    """Returns errors for siblings who are not twins born less than 9 months apart"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for fam in families.values():
        if len(fam.child_ids) > 1:
            children = [individuals.get(child_id) for child_id in fam.child_ids]
            children.sort(key=lambda x: x.birth or date(1,1,1))
            children = list(filter(lambda c: c.birth is not None, children))
            for i in range(1,len(children)):
                twins = datehelpers.dates_within(children[i-1].birth, children[i].birth, 1, 'days')
                lessThan9Months = datehelpers.dates_within(children[i-1].birth, children[i].birth, 9, 'months')
                if lessThan9Months and not twins:
                    errorMessage = f'Siblings {children[i-1]}, {children[i]} born less than 9 months apart {children[i-1].birth}, {children[i].birth}'
                    errors.append(GedcomError(GedcomError.ErrorType.error, 'US10', fam, errorMessage))

    return errors