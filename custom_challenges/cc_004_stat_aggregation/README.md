# Challenge 004 – Monte Carlo Simulation Statistics

You are given a dataset `monte_carlo_simulations.csv` which contains Monte Carlo simulations of NPV (Net Present Value,
i.e., future return) and R&D (Research and Development) costs for seven different projects in your company.
Your task is to calculate the returns and risks for each possible portfolio of two projects and to find the optimal ones
under given constraints.

## Data Overview

You can access the dataset using the path `./data/monte_carlo_simulations.csv`.
The dataset consists of the following four variables:

- **project_id**: a column of project IDs (there are seven unique values)
- **simulation_id**: a simulation number (for each project ID there are 1001 simulations of different realizations of
  NPV and R&D values)
- **npv**: a numeric column of realizations of Monte Carlo simulations of NPV
- **rnd**: a numeric column of realizations of Monte Carlo simulations of R&D costs

The dataset has 7007 rows, with 1001 simulations of NPV and R&D values for each project.

## Task Details

In order to complete the task you must write a function named `markowitz_monte_carlo_simulations` that takes two
arguments, `max_cost` and `min_return`, and performs the following steps:

1. **Calculate a series with mean NPV value (from all 1001 simulations) for each project.**
2. **Calculate a data frame with NPV covariances between each pair of projects.**
3. **Calculate a series with mean R&D value (from all 1001 simulations) for each project.**
4. **Create a list with all valid portfolio combinations**, i.e., a list with binary vectors of length 7 (number of
   projects), where value 1 in the ith place indicates that the ith project is in a portfolio and 0 otherwise. Use
   the `itertools.product()` function to perform this step. Make sure that you remove the empty portfolio (all zeros)
   from the list.
5. For each portfolio:
    - Calculate its total return (as a sum of mean NPV values for projects that are included in the portfolio).
    - Calculate its variance (using the equation below).
    - Calculate its total cost (as a sum of mean R&D values for projects that are included in the portfolio).
    - **Equation for calculating variance**: `Var_portfolio = w.T @ Σ @ w`,
      where:
        - `w` is a vector defining a portfolio, where `w_i` is either 0 or 1
        - `Σ` is the covariance matrix of NPV

   Save all these values in a data frame with the following columns:
    - **portfolio**: contains tuple values for portfolios' combinations
    - **return**: contains numeric values for portfolios' total returns
    - **variance**: contains numeric values for portfolios' variances
    - **cost**: contains numeric values for portfolios' total costs
6. **Find the portfolio with the maximum return under the constraint that its maximum cost is no greater
   than `max_cost`** (the function's argument).
7. **Find the portfolio with the minimum variance under the constraint that its minimum return is no smaller
   than `min_return`** (the function's argument).

The function `markowitz_monte_carlo_simulations` should return a dictionary with the following elements:

- **mean_npv**: a series with mean NPV values (indices should be named according to the corresponding projects' IDs)
- **cov_npv**: a data frame with covariances between NPV values for each project combination (both indices and column
  names should be named according to the projects' IDs)
- **mean_rnd**: a series with mean R&D values (indices should be named according to the corresponding projects' IDs)
- **portfolio_df**: the data frame created in step 5, with portfolios' returns, variances and costs
- **max_return**: a dictionary with two elements:
    - **portfolio**: tuple of an optimal portfolio as found in step 6
    - **return**: its return
- **min_variance**: a dictionary with two elements:
    - **portfolio**: tuple of an optimal portfolio as found in step 7
    - **variance**: its return

### Assumptions

- Assume that, for points 6 and 7, the values of `min_return` and `max_cost` will be set always to find the optimum
  portfolio; you don't have to consider corner cases.

### Hints

- All allowed packages have been loaded in the initial solution.
- You may want to use `mean()` and `cov()` methods to achieve steps 1 to 3.

### Examples

Here's the exemplary structure of the output:

```
>>> output = markowitz_monte_carlo_simulations(10000, 0)

>>> output.keys()
dict_keys(['mean_npv', 'cov_npv', 'mean_rnd', 'portfolio_df', 'max_return', 'min_variance'])

>>> output['mean_npv']
project_id
p_107904   -128.567433
p_478797   -106.447552
...        ...

>>> output['cov_npv']
project_id      p_107904      p_478797   p_547185     p_637525    p_729790    p_761841     p_857195
project_id
p_107904    16636.111698    -49.089210  31.524961  -159.060953  -16.431836   70.779268   305.422171
p_478797      -49.089210  13066.989497  -4.728636     3.108741   33.707650  -12.441986   379.278867
...                  ...           ...        ...          ...         ...         ...          ...

>>> output['portfolio_df']
                 portfolio      return      variance        cost
0    (0, 0, 0, 0, 0, 0, 1)  214.135864   5917.019522   23.391608
1    (0, 0, 0, 0, 0, 1, 0)   52.218781    209.381087   10.880120
2    (0, 0, 0, 0, 0, 1, 1)  266.354645   6144.387101   34.271728
                       ...         ...           ...         ...

>>> output['max_return']
{'portfolio': (0, 0, 1, 1, 1, 1, 1), 'return': 416.8831168831168}
```

## Available Packages and Libraries

- pandas (1.4.3)
- numpy (1.23.0)
- itertools