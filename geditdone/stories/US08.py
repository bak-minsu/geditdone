def birth_before_parent_marriage(parser):
    """Makes sure birth happens after parent marriage"""
    individuals = parser.individuals
    families = parser.families
    for fam in families.values():
        if fam.child_ids != []:
            for childID in fam.child_ids:
                if individuals.get(childID).birth is not None and \
                    fam.married is not None and \
                    individuals.get(childID).birth <= fam.married:
                        return False
                elif individuals.get(childID).birth is None and \
                    fam.married is not None:
                        return False
    return True