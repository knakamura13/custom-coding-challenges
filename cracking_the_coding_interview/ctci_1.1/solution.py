class Solution:
    def __init__(self, _input):
        self.input = _input

    def solve_problem(self):
        """Solution: O(n^2) time, O(n) space."""
        chars = ''

        for char in self.input:
            if char in chars:
                return False
            chars += char

        return True

    def _variant_optimal_time(self):
        """Variant: O(n) time, O(n) space."""
        chars = set()
        for char in self.input:
            if char in chars:
                return False
            chars.add(char)
        return True

    def _variant_optimal_space(self):
        """Variant: O(n^2) time, O(n) space."""
        for i in range(len(self.input)):
            if self.input[i] in self.input[i + 1:]:
                return False
        return True

    def _variant_dynamic_programming(self):
        """Variant: O(n^2) time, O(n) space."""
        n = len(self.input)
        dp = [[False] * n for _ in range(n)]

        # Fill the DP table
        for i in range(n):
            for j in range(i + 1, n):
                if self.input[i] == self.input[j]:
                    dp[i][j] = True

        # Check if there are any duplicates
        for i in range(n):
            for j in range(i + 1, n):
                if dp[i][j]:
                    return False

        return True
