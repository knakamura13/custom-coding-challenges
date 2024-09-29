class Solution:
    def __init__(self, _input):
        self.input = _input

    def solve_problem(self):
        """Solution: O(n log n) time, O(n) space."""
        sorted_list = sorted(self.input)
        prev_smallest = 0

        for num in sorted_list:
            if num > 0 and num != prev_smallest:
                if num != prev_smallest + 1:
                    return prev_smallest + 1
                prev_smallest = num

        return prev_smallest + 1 if prev_smallest > 0 else 1

    def _variant_optimal_space(self):
        """Solution: O(n) time, O(1) space."""
        n = len(self.input)

        # Step 1: Mark elements out of range and filter out non-positive numbers
        for i in range(n):
            if self.input[i] <= 0 or self.input[i] > n:
                self.input[i] = n + 1

        # Step 2: Use the index as a hash to mark the presence of numbers
        for i in range(n):
            num = abs(self.input[i])
            if num <= n:
                self.input[num - 1] = -abs(self.input[num - 1])

        # Step 3: Find the first index which is not marked
        for i in range(n):
            if self.input[i] > 0:
                return i + 1

        return n + 1
