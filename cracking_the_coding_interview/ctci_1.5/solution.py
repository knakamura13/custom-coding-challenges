class Solution:
    def __init__(self, _input):
        self.strings = _input.split(',')
        self.s0 = self.strings[0]
        self.s1 = self.strings[1]

    def solve_problem(self):
        """Solution: O(n) time, O(n) space."""
        # Check if strings are identical (zero edits)
        if self.s0 == self.s1:
            return True

        if abs(len(self.s0) - len(self.s1)) > 1:
            return False

        for idx in range(min(len(self.s0), len(self.s1)) + 1):
            if idx < len(self.s0) and idx < len(self.s1):
                # Return True if inserting an arbitrary character to either string would make them equal
                s0_replaced = f'{self.s0[:idx]}*{self.s0[idx + 1:]}'
                s0_inserted = f'{self.s0[:idx]}*{self.s0[idx:]}'
                s1_replaced = f'{self.s1[:idx]}*{self.s1[idx + 1:]}'
                s1_inserted = f'{self.s1[:idx]}*{self.s1[idx:]}'
                if (s0_replaced == s1_replaced
                        or s0_replaced == s1_inserted
                        or s0_inserted == s1_replaced
                        or s0_inserted == s1_inserted):
                    return True
                continue

            # Return True if removing an arbitrary character from either string would make them equal
            s0_removed = f'{self.s0[:idx]}{self.s0[idx + 1:]}'
            s1_removed = f'{self.s1[:idx]}{self.s1[idx + 1:]}'
            if s0_removed == self.s1 or s1_removed == self.s0:
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
        if len_s0 > len_s1:
            longer, shorter = self.s0, self.s1
        else:
            longer, shorter = self.s1, self.s0

        # Initialize variables to track indices and a flag for finding a difference
        found_difference = False
        index_longer, index_shorter = 0, 0

        # Iterate through both strings simultaneously
        while index_shorter < len(shorter) and index_longer < len(longer):
            if shorter[index_shorter] != longer[index_longer]:
                if found_difference:
                    # More than one mismatch found
                    return False

                # Record the mismatch
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
