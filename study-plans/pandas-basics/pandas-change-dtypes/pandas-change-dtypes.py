import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    df = pd.DataFrame(data)
    before = {col: str(dtype) for col, dtype in df.dtypes.items()}
    df[column] = df[column].astype(target_type)
    after = {col: str(dtype) for col, dtype in df.dtypes.items()}

    return [before, after]