import numpy as np


def solve(x):
    """Implement ReLU Activation from the mathematical contract in README.md."""
    #x = np.array(x)
    return np.maximum(x,0)
