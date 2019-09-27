import gedcom_db

class ValidatorMinsu:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families
        self.db = gedcom_db.GedcomDatabase(individuals, families)

    def marriage_before_divorce(self):
        """Makes sure marriage come before a divorce"""
        print("Marriage before divorse")
        return True

    def marriage_before_death(self):
        """Makes sure mariages come before death"""
        print("Marriage before death")
        return True

    # TODO: Return an error when invalid
    def validate(self):
        tests = [self.marriage_before_death, self.marriage_before_divorce]
        for test in tests:
            if not test():
                print("Invalid!")
                break