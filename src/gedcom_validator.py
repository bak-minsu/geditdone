class Validator:
    def __init__(self, individuals, families):
        """Initializes the class with families and individuals"""
        self.individuals = individuals
        self.families = families

    # TODO: Return an error when invalid
    def validate(self):
        tests = []
        for test in tests:
            if not test():
                print("Invalid!")
                break