from geditdone.error_objects import GedcomError, ErrorType

""" 
All individual IDs should be unique
and all family IDs should be unique

Duplicates are marked in lines 157-163 of ./gedcom_parser.py
"""
def unique_ids(parser):
    errors = []

    for individual in parser.individuals.values():
        if individual.duplicates > 0:
            errMessage = f'ID {individual.id} is non-unique and shared with {individual.duplicates} other individual(s).'
            errors.append(GedcomError(ErrorType.error, 'US22', individual, errMessage))
    for family in parser.families.values():
        if family.duplicates > 0:
            errMessage = f'ID {family.id} is non-unique and shared with {family.duplicates} other families.'
            errors.append(GedcomError(ErrorType.error, 'US22', family, errMessage))
    return errors