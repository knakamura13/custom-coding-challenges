class Solution:
    def __init__(self, _input):
        self.word_a, self.word_b = _input.split('\n')

    def solve_problem(self):
        """Solution: O(n?) time, O(n?) space."""
        if len(self.word_a) != len(self.word_b):
            return False

        if set(self.word_a) == set(self.word_b):
            return True

        char_counts_a, char_counts_b = {}, {}

        for char in self.word_a:
            char_counts_a[char] = 0 if char not in char_counts_a.keys() else char_counts_a[char] + 1

        for char in self.word_b:
            char_counts_b[char] = 0 if char not in char_counts_b.keys() else char_counts_b[char] + 1

        return char_counts_a == char_counts_b
