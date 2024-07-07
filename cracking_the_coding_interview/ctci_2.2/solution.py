import utils


class Solution:
    def __init__(self, _input):
        input_list, k = _input
        self.linked_list = utils.list_to_linkedlist(input_list)
        self.k = k

    def solve_problem(self):
        """Solution: O(n) time, O(1) space."""
        slow = self.linked_list.head
        fast = slow

        # Move fast pointer k-steps ahead of slow
        for _ in range(self.k):
            if not fast:
                # Edge case: k is larger than the length of the list
                return None

            fast = fast.next

        # Advance both pointers until fast reaches the end, with slow still k-steps behind
        while fast:
            slow, fast = slow.next, fast.next

        # Slow is now at the kth-to-last element
        return slow.data

    def _alternative_problem_return_nodes_k_through_n(self):
        """
        Solution: O(n) time, O(1) space.
        I initially misinterpreted the prompt, returning a modified linked-list containing elements k...n.
        """
        if self.k == 1:
            return self.linked_list.to_list()

        # Delete the first node if we're not returning the entire list
        curr = self.linked_list.head.next
        prev = self.linked_list.head
        prev.next = curr.next
        self.linked_list.head = curr
        idx = 2

        while curr and curr.next:
            if idx < self.k:
                # Delete the current Node
                curr = self.linked_list.head.next
                prev = self.linked_list.head
                prev.next = curr.next
                self.linked_list.head = curr

            # Continue to the next Node
            curr = curr.next
            idx += 1

        # Edge case: return empty list if target is beyond the length of the list
        if self.k > idx:
            return []

        return self.linked_list.to_list()
