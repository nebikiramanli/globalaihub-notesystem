import pandas as pd
EXCEL_OVER_COLUMN_WIDTH = 5

def excel_col(col):
    """Covert 1-relative column number to excel-style column label."""
    quot, rem = divmod(col-1,26)
    return excel_col(quot) + chr(rem+ord('A')) if col!=0 else ''

def read_excel(file_path):
    """
    Reads an excel file and returns a pandas dataframe
    """
    return pd.read_excel(file_path)

def write_excel(file_path, dataframe):
    """
    Writes a pandas dataframe to an excel file

    """
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name='notes', index=False)

    for column in dataframe:
        column_width = max(dataframe[column].astype(str).map(len).max(), len(column)) + EXCEL_OVER_COLUMN_WIDTH
        col_idx = excel_col(dataframe.columns.get_loc(column) + 1 )
        writer.sheets['notes'].set_column(f"{col_idx}:{col_idx}", column_width)

    writer.save()

    

