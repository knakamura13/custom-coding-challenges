class Solution:
    def __init__(self, _input):
        self.original_str = _input

    def solve_problem(self):
        """Solution: O(n) time, O(n) space."""
        if len(self.original_str) <= 2:
            return self.original_str

        compressed_str_list = []
        consecutive_chars_count = 1

        for i in range(1, len(self.original_str)):
            curr_char, prev_char = self.original_str[i], self.original_str[i - 1]

            if curr_char == prev_char:
                consecutive_chars_count += 1
            else:
                compressed_str_list.append(prev_char + str(consecutive_chars_count))
                consecutive_chars_count = 1

            if i == len(self.original_str) - 1:
                compressed_str_list.append(curr_char + str(consecutive_chars_count))

        compressed_str = ''.join(compressed_str_list)

        if len(compressed_str) >= len(self.original_str):
            return self.original_str

        return compressed_str
