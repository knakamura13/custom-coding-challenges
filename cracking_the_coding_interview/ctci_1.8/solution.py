class Solution:
    def __init__(self, _input):
        self.input = _input.copy()

    def solve_problem(self):
        """Solution: O(n * m) time, O(m + n) space."""
        m = len(self.input)
        n = len(self.input[0])

        zero_row_indices = set()
        zero_col_indices = set()

        for row in range(m):
            for col in range(n):
                if self.input[row][col] == 0:
                    zero_row_indices.add(row)
                    zero_col_indices.add(col)

        for zero_row in zero_row_indices:
            for col in range(m):
                self.input[zero_row][col] = 0

        for row in range(m):
            for zero_col in zero_col_indices:
                self.input[row][zero_col] = 0

        return self.input

    def _variant_optimal_space(self):
        """Solution: O(n * m) time, O(1) space."""
        m = len(self.input)
        n = len(self.input[0])

        # Check if the first row and first column need to be zeroed
        zero_first_row = any(self.input[0][col] == 0 for col in range(n))
        zero_first_col = any(self.input[row][0] == 0 for row in range(m))

        # Use the first row and column to store zero indicators
        for row in range(1, m):
            for col in range(1, n):
                if self.input[row][col] == 0:
                    self.input[0][col] = 0
                    self.input[row][0] = 0

        # Apply the zero indicators to the matrix
        for row in range(1, m):
            if self.input[row][0] == 0:
                self.input[row][:] = [0] * n

        for col in range(1, n):
            if self.input[0][col] == 0:
                for row in range(m):
                    self.input[row][col] = 0

        # Zero out the first row and first column if needed
        if zero_first_row:
            self.input[0][:] = [0] * n
        if zero_first_col:
            for row in range(m):
                self.input[row][0] = 0

        return self.input
