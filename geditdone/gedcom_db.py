import pandas as pd
from prettytable import PrettyTable

class GedcomDatabase:

    def __init__(self, parser):
        """Individual pandas dataframes for individual and family"""
        # To understand how to use these, look up "Pandas Dataframes"
        self.individuals = self.gen_individual_dict(parser.individuals)
        self.families = self.gen_families_dict(parser.families)
        
    def gen_individual_dict(self, individuals):

        all_ids = []
        all_names = []
        all_sexes = []
        all_births = []
        all_deaths = []
        all_famc = []
        all_fams = []
        all_references = []

        for ID, individual in individuals.items():
            all_ids.append(ID)
            all_names.append(individual.name)
            all_sexes.append(individual.sex)
            all_births.append(individual.birth)
            all_deaths.append(individual.death)
            all_famc.append(individual.famc)
            all_fams.append(individual.fams)
            all_references.append(individual)

        data = {
            "ID": all_ids, 
            "name": all_names,
            "sex": all_sexes, 
            "birth": all_births,
            "death": all_deaths, 
            "famc": all_famc, 
            "fams": all_fams,
            "reference": all_references,    # Reference to the Individual class
        }
        return pd.DataFrame(data)

    def gen_families_dict(self, families):

        all_ids = []
        all_children = []
        all_husbands = []
        all_wives = []
        all_marriages = []
        all_divorces = []
        all_references = []

        for ID, family in families.items():
            all_ids.append(ID)
            all_children.append(family.child_ids)
            all_husbands.append(family.husband_id)
            all_wives.append(family.wife_id)
            all_marriages.append(family.married)
            all_divorces.append(family.divorced)
            all_references.append(family)

        data = {
            "ID": all_ids,
            "husband_id": all_husbands,
            "wife_id": all_wives,
            "married": all_marriages,
            "divorced": all_divorces,
            "children": all_children,
            "reference": all_references,    # Reference to the Family class
        }
        return pd.DataFrame(data)
    
    def print_table(self, dataframe, table_name):
        pt = PrettyTable()
        columns = list(dataframe.columns) 
        columns.remove("reference") # Reference to individual/family class is unnecessary
        pt.field_names = columns
        for index, row in dataframe.iterrows():
            add_row_args = ""
            for index, column in enumerate(columns):
                if index == 0:
                    add_row_args += "["
                else:
                    add_row_args += ","
                add_row_args += "row['" + column + "']"
            add_row_args += "]"
            eval("pt.add_row({})".format(add_row_args))
        print(pt)

    def print_prettytable(self):
        self.print_table(self.individuals, "Individuals")
        self.print_table(self.families, "Families")