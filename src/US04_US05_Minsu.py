class ValidatorMinsu:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families

    def marriage_before_divorce(self):
        """Makes sure marriage come before a divorce"""
        pass

    def marriage_before_death(self):
        """Makes sure mariages come before death"""
        pass

    def validate(self):
        self.marriage_before_death()
        self.marriage_before_divorce()