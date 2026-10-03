import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    l = len(data)
    s = sorted(data)
    # median
    if l % 2 == 0:
        median = (s[l // 2 - 1] + s[l // 2]) / 2
    else:
        median = s[l // 2]
    # mean
    mean = sum(data) / l 
    # mode 
    mode = max(s, key = s.count)
    # variance
    variance = sum((x - mean) ** 2 for x in data) / l
    # standard deviation
    standard_deviation = variance ** 0.5
    # percentiles
    p25 = s[int(l*0.25)]
    p50 = s[int(l*0.50)]
    p75 = s[int(l * 0.75)]
    interquartile_range = float(p75) - float(p25)

    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': standard_deviation,
        '25th_percentile': float(p25),
        '50th_percentile': median,
        '75th_percentile': float(p75),
        'interquartile_range': interquartile_range




    }
