# Coding Challenges

This is a repository for solving coding challenges with Python.

## Dependencies

The dependencies for this project are:

- python=3.11
- jupyter
- matplotlib
- numpy
- pandas
- scikit-learn
- scipy
- seaborn
- pip
- pytest

To manage dependencies, a `requirements.yml` file is provided to create a Conda environment:

```yaml
name: coding-challenges
channels:
  - defaults
dependencies:
  - python=3.11
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - scikit-learn
  - scipy
  - seaborn
  - pip
  - pip:
      - pytest
```

## Getting Started

### Setting up the environment

1. Install [Anaconda](https://www.anaconda.com/products/distribution)
   or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Create a new Conda environment using the provided `requirements.yml` file:

   ```bash
   conda env create --file environment.yml
   ```

3. Activate the newly created environment:

   ```bash
   conda activate coding-challenges
   ```

### Running a coding challenge

Each coding challenge is placed in its own directory.
Each challenge directory contains a solution file (`solution.py`), a test file (`test_solution.py`), and an input
file (`input.txt`).

To run the tests for a specific challenge, navigate to its directory and run pytest:

```bash
pytest test_solution.py
```

Pytest will discover and run the tests, reporting the results in the terminal.

### Creating a new coding challenge

To create a new coding challenge:

1. Duplicate the `challenge_template` directory.
2. Modify the `solution.py` and `input.txt` files as necessary to fit your new challenge.

Update the `input.txt` file with your test cases following this specific format:

- The `input.txt` file is separated into multiple test cases using the delimiter `'---'`.
- Each test case contains the input followed by the expected output on the following line.
- Each line is execute as Python code, so the input and output lines must be valid code.

Here's an example `input.txt`:

```
[1, 2]
3
---
[[1, 2, 3], [4, 5, 6]
21
```

In this example, there are two test cases:

- Test case #1: the input is `[1, 2]` and the expected output is `3`.
- Test case #2: the input is `[[1 2 3], [4 5 6]]` and the expected output is `21`.
