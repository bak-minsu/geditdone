from geditdone.error import ErrorCollector, ErrorType

def marriage_before_divorce(parser):
    """Makes sure marriage come before a divorce"""
    families = parser.families

    for family in families.values():
        if family.married is not None and \
            family.divorced is not None and \
            family.married >= family.divorced:
                errorMessage = f'Marriage date {family.married} is after divorce date {family.divorced}'
                ErrorCollector.add_error(ErrorType.error, 'US04', family, errorMessage)
        elif family.married is None and family.divorced is not None:
                errorMessage = f'Marriage date is None while divorce date is not.'
                ErrorCollector.add_error(ErrorType.error, 'US04', family, errorMessage)