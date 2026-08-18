import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    new_col = column + "_transformed"
    if operation == "normalize":
        mi = min(df[column])
        mx = max(df[column])
        df[new_col] = round((df[column] - mi) / (mx - mi), 4)
    elif operation == "rank":
        df[new_col] = df[column].rank()
    elif operation == "cumsum":
        df[new_col] = df[column].cumsum()
    elif operation == "double":
        df[new_col] = df[column] * 2
    else:
        raise ValueError("Unknown operation")

    return df.to_dict("list")