# Coding Challenges

This is a repository for solving coding challenges in Python 3.10.12.

## Dependencies

The primary dependencies for this project are:

- Python (3.10.12)
- Pip
- Pytest
- Jupyter

To manage dependencies, a `requirements.yml` file is provided to create a Conda environment:

```yaml
name: coding-challenges
channels:
  - defaults
dependencies:
  - python>=3.10.0
  - jupyter
  - pip
    - pytest
```

## Getting Started

### Setting up the environment

1. Install [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Create a new Conda environment using the provided `requirements.yml` file:

   ```bash
   conda env create --file requirements.yml
   ```

3. Activate the newly created environment:

   ```bash
   conda activate coding-challenges
   ```

### Running a coding challenge

Each coding challenge is placed in its own directory. 
Each challenge directory contains a solution file (`solution.py`), a test file (`test_solution.py`), and an input file (`input.txt`).

To run the tests for a specific challenge, navigate to its directory and run pytest:

```bash
pytest test_solution.py
```

Pytest will discover and run the tests, reporting the results in the terminal.

### Creating a new coding challenge

To create a new coding challenge:

1. Duplicate the `challenge_template` directory.
2. Modify the `solution.py` and `input.txt` files as necessary to fit your new challenge.

Remember to update the `input.txt` file with your test cases following this specific format:

- The `input.txt` file is separated into multiple test cases by `'---'`. 
- Each test case contains the input followed by the expected output. 
- The last line of text in each test case is the expected output, and all the preceding lines are the input. 

Here's an example `input.txt`:
```
1 2
3
---
1 2 3
6
```

In this example, there are two test cases: 

- Test case #1: the input is `1 2` and the expected output is `3`. 
- Test case #2: the input is `1 2 3` and the expected output is `6`.

Keep in mind that the `input.txt` file is a text file, which means that its contents are read in as strings. 
This can have implications for how you design your coding challenge and implement your solution. 
Let's use the example of a challenge where the task is to find the sum of the inputs. In order for the test cases in our `input.txt` to work properly, we would need to first convert the input values from strings to integers. 
After performing the necessary calculations to solve the challenge, we would then need to convert the results back into a string format for the output. 
This is because the test will compare this output string with the expected output string in the `input.txt` file. 
Always keep these format considerations in mind when creating new challenges and solutions.
