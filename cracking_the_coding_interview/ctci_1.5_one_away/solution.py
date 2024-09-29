class Solution:
    def __init__(self, _input):
        self.strings = _input
        self.s0 = self.strings[0]
        self.s1 = self.strings[1]

    def solve_problem(self):
        """Solution: O(n^2) time, O(n) space."""
        if self.s0 == self.s1:
            return True

        if abs(len(self.s0) - len(self.s1)) > 1:
            return False

        # Return True if deleting the last character from either string would make them equal
        if self.s0[:-1] == self.s1 or self.s1[:-1] == self.s0:
            return True

        # Return True if inserting OR replacing an arbitrary character in either string would make them equal
        for i in range(len(self.s0) + 1):
            s0_w_insert = self.s0[:i] + '*' + self.s0[i:]
            s1_w_insert = self.s1[:i] + '*' + self.s1[i:]
            s0_w_replace = self.s0[:i] + '*' + self.s0[i + 1:]
            s1_w_replace = self.s1[:i] + '*' + self.s1[i + 1:]
            if s0_w_replace == s1_w_replace or s0_w_replace == s1_w_insert or s0_w_insert == s1_w_replace:
                return True

        return False

    def _variant_optimal_time_and_space(self):
        """Solution: O(n) time, O(1) space."""
        # Calculate the lengths of both strings
        len_s0, len_s1 = len(self.s0), len(self.s1)

        # If the difference in lengths is greater than 1, they can't be one edit away
        if abs(len_s0 - len_s1) > 1:
            return False

        # Identify which string is longer
        longer, shorter = self.s1, self.s0
        if len_s0 > len_s1:
            longer, shorter = self.s0, self.s1

        # Initialize variables to track indices and a flag for finding a difference
        found_difference = False
        index_longer, index_shorter = 0, 0

        # Iterate through both strings simultaneously
        while index_shorter < len(shorter) and index_longer < len(longer):
            if shorter[index_shorter] != longer[index_longer]:
                if found_difference:
                    # More than one mismatch found
                    return False

                # Record the first mismatch
                found_difference = True

                # If lengths are equal, move the shorter index (case of potential replacement)
                if len_s0 == len_s1:
                    index_shorter += 1
            else:
                # If characters are same, move the shorter index
                index_shorter += 1

            # Always move the longer index (covers case of potential insertion/deletion)
            index_longer += 1

        # If the loop completes without finding more than one difference, return True
        return True

    def _variant_dynamic_programming(self):
        """Solution: O(n * m) time, O(n * m) space."""
        len_s0, len_s1 = len(self.s0), len(self.s1)

        # If the difference in lengths is greater than 1, they can't be one edit away
        if abs(len_s0 - len_s1) > 1:
            return False

        # Create a DP table to store the edit distances
        dp = [[0] * (len_s1 + 1) for _ in range(len_s0 + 1)]

        for i in range(len_s0 + 1):
            for j in range(len_s1 + 1):
                if i == 0:
                    dp[i][j] = j  # If s0 is empty, all characters of s1 need to be inserted
                elif j == 0:
                    dp[i][j] = i  # If s1 is empty, all characters of s0 need to be deleted
                elif self.s0[i - 1] == self.s1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # If characters are the same, no new edit
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],  # Deletion
                                       dp[i][j - 1],  # Insertion
                                       dp[i - 1][j - 1])  # Replacement

        # The edit distance is the value in the bottom-right corner of the table
        return dp[len_s0][len_s1] <= 1
