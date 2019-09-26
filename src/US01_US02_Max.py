class ValidatorMax:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families

    def dates_before_current_date(self):
        """Makes sure all dates are before current date"""
        pass

    def birth_before_marriage(self):
        """Makes sure births are before marriage"""
        pass

    def validate(self):
        self.dates_before_current_date()
        self.birth_before_marriage()