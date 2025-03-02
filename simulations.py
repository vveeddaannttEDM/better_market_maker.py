# simulations.py
# Simulations for Better Market Maker and Dynamic Rebate System

def simulate_liquidity_retention(Y0, P0, price_changes, n=4):
    """
    Simulates and prints liquidity retention for different price changes.
    """
    results = [(M, liquidity_retention(Y0, P0, P0 * M, n)) for M in price_changes]
    for M, Y in results:
        print(f"Price Multiplier: {M}, Retained Liquidity: {Y}")

def simulate_impermanent_loss(price_changes, n=4):
    """
    Simulates and prints impermanent loss for different price changes.
    """
    results = [(M, impermanent_loss(M, n)) for M in price_changes]
    for M, IL in results:
        print(f"Price Multiplier: {M}, Impermanent Loss: {IL:.4f}")

def simulate_dynamic_rebate(volumes, V_max):
    """
    Simulates and prints dynamic rebate values for different trading volumes.
    """
    results = [(V, dynamic_rebate(V, V_max)) for V in volumes]
    for V, rho in results:
        print(f"Trading Volume: {V}, Rebate Ratio: {rho:.4f}")
