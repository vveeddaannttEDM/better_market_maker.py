# bmm_model.py
# Implementation of the Better Market Maker (BMM) Algorithm

import numpy as np

def power_law_invariant(X, Y, K, n=4):
    """
    Computes the price of the volatile token using the power-law invariant.
    Xn * Y = K
    """
    return (n * Y) / X

def liquidity_retention(Y0, P0, Pt, n=4):
    """
    Computes stablecoin reserves retained in the pool after a price change.
    """
    return Y0 * (Pt / P0) ** (n / (n + 1))

def impermanent_loss(M, n=4):
    """
    Computes impermanent loss for the given price multiplier M.
    """
    return 1 - (n + 1) ** 2 / (4 * n) * (2 * np.sqrt(M)) / (M + 1)
