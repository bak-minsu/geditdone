from prettytable import PrettyTable

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