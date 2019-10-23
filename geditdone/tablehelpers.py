from prettytable import PrettyTable

class TableHelpers:
    @classmethod
    def print_table(cls, dataframe, table_name):
        pt = PrettyTable()
        columns = list(dataframe.columns) 
        columns.remove("reference") # Reference to individual/family class is unnecessary
        pt.field_names = columns
        for _, row in dataframe.iterrows():
            row_items = []
            for column in columns:
                row_items.append(row[column])
            pt.add_row(row_items)
        print(table_name)
        print(pt)