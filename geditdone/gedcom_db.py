import pandas as pd

class GedcomDatabase:

    def __init__(self, individuals, families):
        self.individuals = self.gen_individual_dict(individuals)
        self.families = self.gen_families_dict(families)
        
    def gen_individual_dict(self, individuals):

        all_names = []
        all_sexes = []
        all_births = []
        all_deaths = []
        all_famc = []
        all_fams = []

        for individual in individuals.values():
            all_names.append(individual.name)
            all_sexes.append(individual.sex)
            all_births.append(individual.birth)
            all_deaths.append(individual.death)
            all_famc.append(individual.famc)
            all_fams.append(individual.fams)

        data = {
            "ID": individuals.keys(), 
            "Name": all_names,
            "Sex": all_sexes, 
            "Birth": all_births,
            "Death": all_deaths, 
            "Famc": all_famc, 
            "Fams": all_fams
        }
        
        return pd.DataFrame(data)

    def gen_families_dict(self, families):

        all_children = []
        all_husbands = []
        all_wives = []
        all_marriages = []
        all_divorces = []

        for family in families.values():
            all_children.append(family.child_ids)
            all_husbands.append(family.husband_id)
            all_wives.append(family.wife_id)
            all_marriages.append(family.married)
            all_divorces.append(family.divorced)

        data = {
            "ID": families.keys(),

            "Husband": all_husbands,
            "Wives": all_wives,
            "Married": all_marriages,
            "Divorce": all_divorces
        }

        return pd.DataFrame(data)