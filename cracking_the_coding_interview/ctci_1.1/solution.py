class Solution:
    """
    Determine if a string has all unique characters using no additional data structures.
    """

    def __init__(self, _input):
        """Initialize the problem and solution."""
        self.input = _input

    def solve_problem(self):
        """Solve the problem."""
        solution = 1
        chars = ''

        for char in self.input:
            if char in chars:
                return 0
            chars += char

        return solution
