

# Better Market Maker (BMM) Algorithm

## Overview
This project implements the **Better Market Maker (BMM) Algorithm** and **Dynamic Rebate System (DRS)** to improve liquidity retention and reduce impermanent loss in decentralized exchanges (DEXs).

## Features
- **Power-law invariant AMM model** for improved liquidity retention.
- **Dynamic rebate system** to incentivize trading activity.
- **Simulations** to evaluate liquidity retention, impermanent loss, and rebate effectiveness.

## Installation
Ensure you have Python installed, then install dependencies:
```bash
pip install numpy
```

## Usage
Run simulations to test the model:
```python
from simulations import simulate_liquidity_retention, simulate_impermanent_loss, simulate_dynamic_rebate

simulate_liquidity_retention(Y0=10000, P0=1, price_changes=[1, 10, 100])
simulate_impermanent_loss(price_changes=[1, 10, 100])
simulate_dynamic_rebate(volumes=[5000, 10000, 20000], V_max=10000)
```

## License
This project is open-source under the MIT License.
