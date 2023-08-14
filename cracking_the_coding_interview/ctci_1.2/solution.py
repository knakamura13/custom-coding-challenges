class Solution:
    def __init__(self, _input):
        self.s1, self.s2 = _input.split('\n')

    def solve_problem(self):
        """Solution: O(n) time, O(n) space."""
        if len(self.s1) != len(self.s2):
            return False

        if set(self.s1) == set(self.s2):
            return True

        char_counts_a, char_counts_b = {}, {}

        for char in self.s1:
            char_counts_a[char] = char_counts_a.get(char, 0) + 1

        for char in self.s2:
            char_counts_b[char] = char_counts_b.get(char, 0) + 1

        return char_counts_a == char_counts_b

    def _variant_optimal_space(self):
        """Variant: O(n) time, O(1) space."""
        if len(self.s1) != len(self.s2):
            return False
        char_counts = [0] * 128  # Assuming ASCII character set
        for char in self.s1:
            char_counts[ord(char)] += 1
        for char in self.s2:
            char_counts[ord(char)] -= 1
            if char_counts[ord(char)] < 0:
                return False
        return True
