from geditdone.gedcom_db import GedcomDatabase

class TestParser:
    def __init__(self, individuals, families):
        self.individuals = individuals
        self.families = families

class TestDatabase:
    def __init__(self, individuals, families):
        self.individuals = GedcomDatabase.gen_individuals(individuals)
        self.families = GedcomDatabase.gen_families(families)