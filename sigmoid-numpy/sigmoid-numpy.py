import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:

    arr = np.array(x)

    result = 1 / (1 + np.exp(-arr))

    if np.isscalar(x):
        return float(result)

    return result
    pass