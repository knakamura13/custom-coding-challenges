import logging
import pytest
from solution import Solution

TEST_CASES_FILENAME = 'input.txt'  # The text file containing test cases.
TEST_CASE_SEPARATOR = '---'  # Delimiter used to separate test cases in text file.


def load_test_cases():
    """
    Load the test cases from the text file. Each test case is defined as a block of text separated by the
    TEST_CASE_SEPARATOR. The last line of each block is treated as the expected output, and all other lines are
    treated as the input.
    """
    # Attempt to open the file and read its contents.
    try:
        with open(TEST_CASES_FILENAME, 'r') as file:
            content = file.read().strip()
    except FileNotFoundError:
        logging.error(f"{TEST_CASES_FILENAME} file not found.")
        return []

    # Split the content into different blocks, each representing a test case.
    blocks = content.split(TEST_CASE_SEPARATOR)

    # For each block, split it into input and expected output at the last newline character.
    test_cases = []
    for i, block in enumerate(blocks, 1):
        block = block.rstrip()  # Remove any trailing whitespace characters.
        parts = block.rsplit('\n', 1)  # Attempt to split the block into input and output.

        # If the block could not be split into input and output, print an error message and skip this test case.
        if len(parts) != 2:
            logging.error(f"Test case #{i} is malformed (missing input, output, or both).")
            continue

        test_input, test_output = parts
        test_cases.append((test_input.strip(), test_output.strip()))

    return test_cases


@pytest.mark.parametrize("test_case_input,expected_output", load_test_cases())
def test_solve_problem(test_case_input, expected_output):
    # Initialize a Solution instance with the input from the test case.
    solution_instance = Solution(test_case_input)

    # Assert that the output from the solve_problem method is equal to the expected output from the test case.
    assert solution_instance.solve_problem() == expected_output
