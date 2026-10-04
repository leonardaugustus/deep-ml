def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    r =  []
    l = len(samples)
    for i in set(samples):
        r.append((i, samples.count(i) / l))
    # eaisest way to sort for the probabilities is to sort by the first element of the tuple
    r.sort(key = lambda x: x[0], reverse = False)

    return r
    
        



