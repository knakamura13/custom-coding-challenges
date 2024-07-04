class Solution:
    def __init__(self, _input):
        self.input = _input

    def solve_problem(self):
        """Solution: O(n^2) time, O(1) space."""
        n = len(self.input)

        # Transpose the matrix
        for i in range(n):
            for j in range(i):
                self.input[i][j], self.input[j][i] = self.input[j][i], self.input[i][j]

        # Reverse each row
        for i in range(n):
            self.input[i].reverse()

        return self.input
