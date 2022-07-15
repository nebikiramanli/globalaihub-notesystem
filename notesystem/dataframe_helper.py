import pandas as pd


def to_dataframe(data):
    """
    Convert a list of dictionaries to a pandas dataframe.
    """
    return pd.DataFrame(data)

def check_dataframe(dataframe):
    """
    Check if the dataframe is empty.
    returns True if the dataframe is empty, False otherwise.
    """
    return dataframe.empty

def insert_dataframe(dataframe, data):
    """
    Insert a dataframe to another dataframe.
    """
    return dataframe.append(data)

def insert_column(dataframe, column_name, data):
    """
    Insert a column to a dataframe.
    """
    dataframe[column_name] = data
    return dataframe

def delete_column(dataframe, column_name):
    """
    Delete a column from a dataframe.
    """
    del dataframe[column_name]
    return dataframe
