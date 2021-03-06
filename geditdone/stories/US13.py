from geditdone.error_objects import GedcomError, ErrorType
from geditdone.datehelpers import DateHelpers
from datetime import date

def sibling_spacing(parser):
    """Returns errors for siblings who are not twins born less than 8 months apart"""
    individuals = parser.individuals
    families = parser.families
    errors = []

    for fam in families.values():
        if len(fam.child_ids) > 1:
            children = [individuals.get(child_id) for child_id in fam.child_ids]
            children.sort(key=lambda x: x.birth or date(1,1,1))
            children = list(filter(lambda c: c.birth is not None, children))
            for i in range(1,len(children)):
                twins = DateHelpers.dates_within(children[i-1].birth, children[i].birth, 2, 'days')
                lessThan9Months = DateHelpers.dates_within(children[i-1].birth, children[i].birth, 8, 'months')
                if lessThan9Months and not twins:
                    errorMessage = f'Siblings {children[i-1]}, {children[i]} born less than 8 months apart {children[i-1].birth}, {children[i].birth}'
                    errors.append(GedcomError(ErrorType.error, 'US13', fam, errorMessage))

    return errors