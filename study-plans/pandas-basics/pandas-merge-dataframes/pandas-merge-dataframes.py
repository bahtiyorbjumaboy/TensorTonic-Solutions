import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    l = pd.DataFrame(left)
    r = pd.DataFrame(right)

    return pd.merge(l, r, on=on, how=how).to_dict("list")