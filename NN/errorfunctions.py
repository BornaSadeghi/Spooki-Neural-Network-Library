def mean_squared_error(y, y_prime):
    n = len(y)
    assert n == len(y_prime), "Output shape does not match targets"

    error = 0
    for i in range(n):
        error += (y_prime[i]-y[i])**2/n
    return error