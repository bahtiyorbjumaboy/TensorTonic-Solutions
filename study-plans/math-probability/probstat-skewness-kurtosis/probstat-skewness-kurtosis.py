import numpy as np

def skewness_kurtosis(data):
    """
    Returns: dict with 'skewness', 'kurtosis', and interpretation strings.
    """
    mean = np.mean(data)
    s = np.std(data, ddof=1)
    n = len(data)
    z = (data - mean) / s

    g1 = n / ( (n-1) * (n-2) ) * np.sum( z ** 3 )
    g2 = ( ( n * (n+1) ) / ( (n-1) * (n-2) * (n-3) ) ) * np.sum( z ** 4 )
    g2 -= ( 3 * (n-1) ** 2 ) / ( (n-2) * (n-3) )

    if g1 > 0.5:
        skew = "right-skewed"
    elif g1 < -0.5:
        skew = "left-skewed"
    else:
        skew = "approximately symmetric"


    if g2 > 1:
        kurtosis = "leptokurtic"
    elif g2 < -1:
        kurtosis = "platykurtic"
    else:
        kurtosis = "mesokurtic"

    return {
        "skewness": round(g1, 4),
        "kurtosis": round(g2, 4),
        "skew_interpretation": skew,
        "kurtosis_interpretation": kurtosis
    }