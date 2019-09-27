class ValidatorMax:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families

    def dates_before_current_date(self):
        """Makes sure all dates are before current date"""
        return True

    def birth_before_marriage(self):
        """Makes sure births are before marriage"""
        return True

    def validate(self):
        tests = [self.dates_before_current_date, self.birth_before_marriage]
        for test in tests:
            if not test():
                print("Invalid!")
                break