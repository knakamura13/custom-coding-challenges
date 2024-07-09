class Solution:
    def __init__(self, _input):
        self.input = _input

    def solve_problem(self):
        """Solution: O(n) time, O(n) space."""
        sorted_list = sorted(self.input)
        prev_smallest = 0

        for num in sorted_list:
            if num > 0 and num != prev_smallest:
                if num != prev_smallest + 1:
                    return prev_smallest + 1
                prev_smallest = num

        return prev_smallest + 1 if prev_smallest > 0 else 1
