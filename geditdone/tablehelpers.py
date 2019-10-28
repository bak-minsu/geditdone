from prettytable import PrettyTable
from datetime import date

class TableHelpers:

    @classmethod
    def dataframe2table(cls, dataframe, table_name):
        """Converts and Pandas Dataframe to the tables dictionary"""
        pt = PrettyTable()
        pt.title = table_name
        columns = list(dataframe.columns) 
        columns.remove("reference")             # Reference to individual/family class is unnecessary
        pt.field_names = columns                # Set PrettyTable columns headers
        for _, row in dataframe.iterrows():
            row_items = []                      # Convert pandas dataframe row to python list
            for column in columns:
                row_items.append(row[column])
            pt.add_row(row_items)               # Add the list-row to PrettyTable
        return pt

    @classmethod
    def get_row_count(cls, pt):
        """Takes a prettytable as input and returns its rowcount"""
        count = 0
        for _ in pt:
            count += 1
        return count

    @classmethod
    def get_row_field_value(cls, row, field):
        row.border = False
        row.header = False
        row._title = None
        return row.get_string(fields=[field]).strip()
