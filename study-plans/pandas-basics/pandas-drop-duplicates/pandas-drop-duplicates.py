import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    return [before, after, df.to_dict("list")]