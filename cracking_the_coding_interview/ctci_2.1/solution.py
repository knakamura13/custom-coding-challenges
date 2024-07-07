import utils


class Solution:
    def __init__(self, _input):
        self.input = utils.list_to_linkedlist(_input)

    def solve_problem(self):
        """Solution: O(n) time, O(n) space."""
        current = self.input.head
        prev = None
        seen = set()

        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

        return self.input.to_list()

    def _variant_optimal_space_without_buffer(self):
        """Solution: O(n^2) time, O(1) space."""
        current = self.input.head

        while current:
            # Use runner to compare all proceeding nodes with the current node
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next  # Remove duplicate node
                else:
                    runner = runner.next  # Move runner to the next node

            current = current.next  # Move current to the next node

        return self.input.to_list()
