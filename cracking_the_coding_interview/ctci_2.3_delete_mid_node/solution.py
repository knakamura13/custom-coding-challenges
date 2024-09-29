import utils


class Solution:
    def __init__(self, _input):
        input_list, k = _input
        self.linked_list = utils.list_to_linkedlist(input_list)
        self.target = self.linked_list.head

        # Set up the `target` which is the given node that needs to be deleted
        # Note: according to the prompt, the target will never be the first or last element
        for _ in range(k - 1):
            if self.target:
                self.target = self.target.next

    def solve_problem(self):
        """Solution: O(1) time, O(1) space."""
        if self.target.next:
            self.target.data = self.target.next.data
            self.target.next = self.target.next.next

        return self.linked_list.to_list()
