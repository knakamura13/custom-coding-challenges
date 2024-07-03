def clean_string(input_string: str) -> str:
    lower_case_string = input_string.lower()

    # Filter out non-letter characters
    return ''.join([char for char in lower_case_string if char.isalpha()])


class Solution:
    def __init__(self, _input: str):
        self.s = clean_string(_input)

    def solve_problem(self) -> bool:
        """Solution: O(n) time, O(n) space."""
        # Check if empty or single-character
        if len(self.s) <= 1:
            return True

        # Count occurrences of each unique character
        char_count_dict = {}
        for char in self.s:
            char_count_dict[char] = char_count_dict.get(char, 0) + 1

        # Check how many characters have an odd number of occurrences
        num_odd_pairs = 0
        for count in char_count_dict.values():
            if count % 2:
                num_odd_pairs += 1

        return num_odd_pairs <= 1

    def _variant_optimal_code_simplicity(self) -> bool:
        """Solution: O(n) time, O(n) space."""
        if len(self.s) <= 1:
            return True
        char_count = {char: self.s.count(char) for char in set(self.s)}
        num_odd = sum(count % 2 for count in char_count.values())
        return num_odd <= 1
