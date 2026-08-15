import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    element = df.iloc[row, col]
    row_values = df.iloc[row, :]
    col_values = df.iloc[:, col]

    return [element, row_values, col_values]