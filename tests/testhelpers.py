from geditdone.gedcom_db import GedcomDatabase

class TestParser:
    def __init__(self, individuals, families):
        self.individuals = individuals
        self.families = families

class TestDatabase:
    def __init__(self, individuals, families):
        parser = TestParser(individuals, families)
        db = GedcomDatabase(parser)
        self.individuals = db.individuals
        self.families = db.families