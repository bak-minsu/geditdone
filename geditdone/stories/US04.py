def marriage_before_divorce(parser):
    """Makes sure marriage come before a divorce"""
    families = parser.families
    for family in families.values():
        if family.married is not None and \
            family.divorced is not None and \
            family.married >= family.divorced:
            return False
        elif family.married is None and family.divorced is not None:
            return False
    return True