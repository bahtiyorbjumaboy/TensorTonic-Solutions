import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    list_of_dfs = [pd.DataFrame(df) for df in dfs]
    concat_dfs = pd.concat(list_of_dfs, ignore_index=True)
    return [list(concat_dfs.shape), concat_dfs.to_dict("list")]