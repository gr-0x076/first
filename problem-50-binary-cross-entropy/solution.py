import numpy as np

def solve(logits, labels):
    """
    Compute mean binary cross-entropy from real-valued logits and binary labels,
    using a stable logits-based formula (avoiding explicit sigmoid + log).
    """
    logits = np.asarray(logits, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.float64)
    
    loss_per_sample = np.maximum(logits, 0) - logits * labels + np.log1p(np.exp(-np.abs(logits)))
    
    return float(np.mean(loss_per_sample))
