from prettytable import PrettyTable

class TableCollector:
    tables = {}

    @classmethod
    def add_dataframe(cls, dataframe, table_name):
        pt = PrettyTable()
        columns = list(dataframe.columns) 
        columns.remove("reference") # Reference to individual/family class is unnecessary
        pt.field_names = columns
        for _, row in dataframe.iterrows():
            row_items = []
            for column in columns:
                row_items.append(row[column])
            pt.add_row(row_items)
        TableCollector.tables[table_name] = pt

    @classmethod
    def print_all(cls):
        for name, table in TableCollector.tables.items():
            print(name)
            print(table)