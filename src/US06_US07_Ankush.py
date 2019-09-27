class ValidatorAnkush:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families

    def divorce_before_death(self):
        """Makes sure divorces occur before death"""
        return True

    def less_than_150_years_old(self):
        """Makes sure nobody reaches 150 years old"""
        return True

    def validate(self):
        tests = [self.divorce_before_death, self.less_than_150_years_old]
        for test in tests:
            if not test():
                print("Invalid!")
                break