import numpy as np
import pandas as pd
from itertools import product


def markowitz_monte_carlo_simulations(max_cost, min_return) -> dict:
    """Solution: O(n) time, O(n) space."""
    # Step 1: Load the dataset
    file_path = 'monte_carlo_simulations.csv'
    df = pd.read_csv(file_path)

    # Step 2: Calculate mean NPV for each project
    mean_npv = df.groupby('project_id')['npv'].mean()

    # Step 3: Calculate covariance matrix of NPV
    npv_pivot = df.pivot(index='simulation_id', columns='project_id', values='npv')
    cov_npv = npv_pivot.cov()

    # Step 4: Calculate mean R&D cost for each project
    mean_rnd = df.groupby('project_id')['rnd'].mean()

    # Step 5: Generate all valid portfolio combinations
    num_projects = len(mean_npv)
    all_combinations = list(product([0, 1], repeat=num_projects))  # Create all possible combinations
    portfolios = [combo for combo in all_combinations if sum(combo) > 0]  # Exclude the empty portfolio

    # Step 6: Calculate metrics for each portfolio
    portfolio_data = []
    for portfolio in portfolios:
        portfolio_array = np.array(portfolio)

        # Calculate total return
        total_return = sum(portfolio_array * mean_npv.values)

        # Calculate total cost
        total_cost = sum(portfolio_array * mean_rnd.values)

        # Calculate variance
        portfolio_variance = portfolio_array @ cov_npv.values @ portfolio_array

        # Append the current portfolio data to the result list
        portfolio_data.append((tuple(portfolio), total_return, portfolio_variance, total_cost))

    portfolio_df = pd.DataFrame(portfolio_data, columns=['portfolio', 'return', 'variance', 'cost'])

    # Step 7: Find optimal portfolios
    max_return_portfolio = portfolio_df[portfolio_df['cost'] <= max_cost] \
        .sort_values(by='return', ascending=False) \
        .iloc[0]
    min_variance_portfolio = portfolio_df[portfolio_df['return'] >= min_return] \
        .sort_values(by='variance', ascending=True) \
        .iloc[0]

    return {
        'mean_npv': mean_npv,
        'cov_npv': cov_npv,
        'mean_rnd': mean_rnd,
        'portfolio_df': portfolio_df,
        'max_return': {
            'portfolio': max_return_portfolio['portfolio'],
            'return': max_return_portfolio['return']
        },
        'min_variance': {
            'portfolio': min_variance_portfolio['portfolio'],
            'variance': min_variance_portfolio['variance']
        }
    }


if __name__ == '__main__':
    output = markowitz_monte_carlo_simulations(max_cost=10000, min_return=0)
    print(output)
