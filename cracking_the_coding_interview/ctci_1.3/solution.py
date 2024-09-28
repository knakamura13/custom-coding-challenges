class Solution:
    def __init__(self, _input):
        self.s, self.true_length = _input
        self.true_length = int(self.true_length)
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

    def _variant_optimal_time_and_space(self):
        """Variant: O(n) time, O(n) space."""
        char_list = list(self.s)
        spaces_count = char_list.count(self.SPACE_DECODED)
        extra_chars = spaces_count * (len(self.SPACE_ENCODED) - 1)
        new_length = self.true_length + extra_chars

        # Create a list large enough to store the encoded space characters
        char_list.extend([''] * extra_chars)

        # Iterate backwards
        j = new_length - 1
        for i in range(self.true_length - 1, -1, -1):
            if char_list[i] == self.SPACE_DECODED:
                char_list[j - 2:j + 1] = self.SPACE_ENCODED
                j -= 3
            else:
                char_list[j] = char_list[i]
                j -= 1

        return ''.join(char_list)

    def _variant_dynamic_programming(self):
        """Variant: O(n) time, O(n) space."""
        dp = [''] * self.true_length

        # Fill the DP table with the original characters
        for i in range(self.true_length):
            dp[i] = self.s[i]

        # Create a result list to store the final characters
        result = []

        # Iterate through the DP table and replace spaces with '%20'
        for i in range(self.true_length):
            if dp[i] == self.SPACE_DECODED:
                result.append(self.SPACE_ENCODED)
            else:
                result.append(dp[i])

        return ''.join(result)
