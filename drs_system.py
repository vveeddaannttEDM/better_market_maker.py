# drs_system.py
# Implementation of the Dynamic Rebate System (DRS)

def dynamic_rebate(V, V_max, base_rebate=0.3, max_rebate=0.4):
    """
    Computes the rebate ratio dynamically based on trading volume.
    """
    rho = base_rebate + 0.1 * (1 - V / V_max)
    return max(base_rebate, min(rho, max_rebate))

def transaction_fee(V, gamma=0.005):
    """
    Calculates the transaction fee based on trading volume.
    """
    return gamma * V

def allocate_fees(F, rho):
    """
    Allocates fees among liquidity providers, traders, and protocol reserves.
    """
    Flp = 0.3 * F  # Liquidity provider share
    Fr = rho * F  # Trader rebate
    Fp = (0.7 - rho) * F  # Protocol reserves
    return Flp, Fr, Fp
