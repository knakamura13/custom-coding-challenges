def is_substring(s1, s2):
    return s2 in s1


class Solution:
    def __init__(self, _input):
        self.s1, self.s2 = _input

    def solve_problem(self):
        """Solution: O(n) time, O(1) space."""
        n = len(self.s1)

        if n != len(self.s2):
            return False

        # Iterate with an expanding window, comparing the first i characters in s1 to the last i characters in s2,
        # and the last n-i characters in s1 to the last n-1 characters in s2
        for i in range(1, n):
            if self.s1[:i] == self.s2[n - i:] and self.s1[i:] == self.s2[:n - i]:
                return True

        return self.s1 == self.s2

    def _variant_optimal_use_of_is_substring(self):
        """Solution: O(n) time, O(1) space."""
        if len(self.s1) != len(self.s2):
            return False

        return is_substring(self.s1 + self.s1, self.s2)
