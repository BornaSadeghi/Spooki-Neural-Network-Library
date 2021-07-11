def mean_squared_error(y, y_prime):
    """
    Return the mean of the squared difference between two vectors of identical size.

    Parameters
    ----------
    y: list
        The expected values of the network.
    y_prime: list
        The predicted values of the network.
    """
    n = len(y)
    assert n == len(y_prime), "Output shape does not match targets"

    error = 0
    for i in range(n):
        error += (y_prime[i]-y[i])**2/n
    return error