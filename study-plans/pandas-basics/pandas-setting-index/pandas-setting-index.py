import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df = pd.DataFrame(data)
    df.set_index(index_col, inplace=True)

    return {
        "index_values": df.index,
        "columns": df.columns.tolist(),
        "data": df.to_dict("list")
    }