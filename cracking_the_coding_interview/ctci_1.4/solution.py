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
            if char not in char_count_dict:
                char_count_dict[char] = 0
            char_count_dict[char] += 1

        # Check if all characters, except one, belong to a pair
        num_odd_pairs = 0
        for char in char_count_dict:
            count = char_count_dict[char]
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
