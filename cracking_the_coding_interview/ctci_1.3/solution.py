class Solution:
    def __init__(self, _input):
        self.s, self.true_length = _input.split('\n')
        self.SPACE_DECODED = ' '
        self.SPACE_ENCODED = '%20'

    def solve_problem(self):
        """Solution: O(n^2) time, O(n) space."""
        extra_chars = 0

        for i, char in enumerate(self.s):
            if char != self.SPACE_DECODED:
                continue

            insert_idx = i + extra_chars
            self.s = self.s[:insert_idx] + self.SPACE_ENCODED + self.s[insert_idx + 1:]
            extra_chars += len(self.SPACE_ENCODED) - 1

        return self.s
