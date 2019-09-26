class ValidatorGaby:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families

    def birth_before_death(self):
        """Makes sure births are before death"""
        pass

    def birth_before_parent_marriage(self):
        """Makes sure birth happens after parent marriage"""
        pass

    def validate(self):
        self.birth_before_death()
        self.birth_before_parent_marriage